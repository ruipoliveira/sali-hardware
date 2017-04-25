
int port_luminosity = 0;
int port_temperature = 3;
int port_level = 2;
int port_valve = 3; 

void setup() {
    pinMode(port_luminosity, OUTPUT);
    pinMode(port_level, OUTPUT);
    pinMode(port_temperature, OUTPUT);
    pinMode(port_valve, OUTPUT); 
    //setWaterValve(port_valve, 1);

    // Start up serial connection
    Serial.begin(9600);
    Serial.flush();
    
}


void loop() {
  
  Serial.print(readTemperature(port_temperature));
  Serial.print(";");
  Serial.print(readWaterLevel(port_level));
  Serial.print(";");
  Serial.print(readLuminosity(port_luminosity));
  Serial.print(";");
  Serial.print(readWaterValve(port_valve));
  Serial.print("\n");
  
  
  int status_valve=10;
  // Read any serial input
  while (Serial.available() > 0){
    status_valve = Serial.read();
  }
  
  if(status_valve=='1'){
    setWaterValve(port_valve, 1); // on
  }
  if(status_valve=='0'){
    setWaterValve(port_valve, 0); // off
  } 
  
}


long readLuminosity(int port){
  return analogRead(port);
}


int readWaterLevel(int port){
  return digitalRead(port);
}

int readWaterValve(int port){
  return digitalRead(port);
}

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

void setWaterValve(int port, int state){
  if (state == 1)
    digitalWrite(port,HIGH);
  else 
    digitalWrite(port,LOW);
}

