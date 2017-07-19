#include <SoftwareSerial.h>  
 
SoftwareSerial mySerial(10, 11); // RX, TX  
int bluetoothData; // variable to receive data 
int port_luminosity = 0;
int port_temperature = 3;
int port_level = 2;
int port_valve = 4; 


void setup(){  
  // Open serial communications and wait for port to open:  
  Serial.begin(115200);  
  Serial.println("Type AT commands!");  
  mySerial.begin(9600);
  pinMode(port_valve, OUTPUT);
  
}

void loop(){  

  if (mySerial.available()){
    bluetoothData=mySerial.read();
    if (bluetoothData=='0'){// valve off 
      setWaterValve(port_valve, 0);
      //mySerial.print("OFF OK!\n");
    }
    if(bluetoothData=='1'){ // valve on 
      setWaterValve(port_valve, 1);
      //mySerial.print("ON OK!\n");
    }
    if (bluetoothData=='2'){// send data
      mySerial.print(readTemperature(port_temperature));
      mySerial.print(";");
      mySerial.print(readWaterLevel(port_level));
      mySerial.print(";");
      mySerial.print(readLuminosity(port_luminosity));
      mySerial.print(";");
      mySerial.print(readWaterValve(port_valve));
      mySerial.print("\n");
    
    }
    
  }
  //delay(100); // prepare for next data ...
      
}// END loop()  


/* read luminosity in port analog */
long readLuminosity(int port){
  float val = 0, val1=0; 
  val = analogRead(port); 
  val1 = ((val-790)*100)/(1022-790); 

  return val1;
}

/* read water level in port digital*/
int readWaterLevel(int port){
  return digitalRead(port);
}

/*read water valve in port digital*/ 
int readWaterValve(int port){
  return digitalRead(port);
}

/*read temperature in port analog */
int readTemperature(int port){
  int Vo;
  float R1 = 10000;
  float logR2, R2, T, Tc, Tf;
  float c1 = 1.009249522e-03, c2 = 2.378405444e-04, c3 = 2.019202697e-07;
  
  Vo = analogRead(port);
  R2 = R1 * (1023.0 / (float)Vo - 1.0);
  logR2 = log(R2);
  T = (1.0 / (c1 + c2*logR2 + c3*logR2*logR2*logR2));
  Tc = T - 273.15;
  Tf = (Tc * 9.0)/ 5.0 + 32.0; 
  
  return Tc;
}

/*function set water valve */
void setWaterValve(int port, int state){
  if (state == 1){
    digitalWrite(port,HIGH);
  }
  else{
    digitalWrite(port,LOW);
  }
}



