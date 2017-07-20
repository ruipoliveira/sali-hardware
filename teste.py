import threading
import socket
import Queue

class ClientThread(threading.Thread):

    def __init__(self,ip,port,clientsocket, in_q, out_q):
        threading.Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.csocket = clientsocket
        self.in_q = in_q
        self.out_q = out_q
        self._tid = "{}:{}".format(ip, port)
        self.daemon = True # Assuming you want the client thread to shutdown when the main thread does
        print ("[+] New thread started for "+ip+":"+str(port))

    def run(self):
        # Stuff happens here
        while True:
            try:
                # Wait 8 seconds for an incoming command
                cmd = self.in_q.get(timeout=8)
                self.csocket.sendall(cmd)
                data = self.csocket.recv(56)
                # Send result to main thread.
                self.out_q.put({'tid' : self._tid, 'data' : data})
            except Queue.Empty:
                # No incoming command after 8 seconds, do a keep-alive instead.
                data = 'someinfo'
                self.csocket.sendall(data)
                data = self.csocket.recv(56)

def handle_socket_connections(resp_queue):
    """ Thread for handling connections from devices. """
    while True:
        host = "127.0.0.1"
        port = 3000
        tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        tcpsock.bind((host,port))   
        tcpsock.listen(5)
        print ("\nListening for incoming connections...")
        (clientsock, (ip, port)) = tcpsock.accept()
        q = Queue.Queue() # Create a Queue for sending commands to this device.
        queues["{}:{}".format(ip,port)] = q
        newthread = ClientThread(ip, port, clientsock, q, resp_queue)
        newthread.start()


queues = {} # dict for managing input queues
resp_queue = Queue.Queue()  # Shared response queue
socket_handler = threading.Thread(target=handle_socket_connections, args=(resp_queue,))
socket_handler.daemon = True
socket_handler.start()

# Wait for user input
while True:
    # example input format: '1.2.3.4:55 ON'
    in_data = raw_input("Enter using the format - <IP>:<Port> <cmd>")
    if in_data == "EXIT":
        break
    ip_port, cmd = in_data.split()
    try:
        queues[ip_port].put(cmd)  # Send command to the appropriate thread.
        result = resp_queue.get()  # Wait for a response.
        print("Got '{data}' from {tid}".format(**result))
    except KeyError:
        print("No conection on {}".format(ip_port))