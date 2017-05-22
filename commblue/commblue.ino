#include <SoftwareSerial.h>  
 
SoftwareSerial mySerial(10, 11); // RX, TX  
int bluetoothData;

void setup()   
{  
// Open serial communications and wait for port to open:  
Serial.begin(115200);  
Serial.println("Type AT commands!");  
// SoftwareSerial "com port" data rate. JY-MCU v1.03 defaults to 9600.  
mySerial.begin(9600);  
}

void loop(){  

if (mySerial.available()){
  bluetoothData=mySerial.read();
  if (bluetoothData=='0'){// valve off 
    mySerial.println("Off");
  }
  if(bluetoothData=='1'){ // valve on 
    mySerial.println("ON!");
  }
  if (bluetoothData=='2'){// valve off 
    mySerial.println("recebe infooooo ");
  }
  
}
delay(100);// prepare for next data ...

 
}// END loop()  
