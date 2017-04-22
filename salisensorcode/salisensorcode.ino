
int port_luminosity = 0;
int port_temperature = 3;
int port_level = 4; 
int port_valve = 2; 

int status_valve; 


void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  //pinMode(port_valve, OUTPUT);

}

void loop() {
  // put your main code here, to run repeatedly:
  
  //setWaterValve(port_valve, 0); 
  //Serial.print(readLuminosity(port_luminosity));
  //Serial.print(";");
  Serial.print(readTemperature(port_temperature));
  //Serial.print(";");
  //Serial.print(readWaterLevel(port_level));
  //Serial.print(";");
  //Serial.print(readWaterValve(port_valve));
  Serial.print("\n");

  //delay(60);        // delay in between reads for stability


    /*
  status_valve = Serial.read();

  if(status_valve=='1'){
    setWaterValve(port_valve, 1); 
  }
  if(status_valve=='0'){
    setWaterValve(port_valve, 0); 
  }
*/

 
  
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

long readLuminosity(int port){
  int value = analogRead(port);
  return value;
}

int readWaterLevel(int port){
  int value = analogRead(port);
  Serial.print(value);
  if (value == 0)
    return 0;
  else
    return 1;
}

int readWaterValve(int port){
  return digitalRead(port);
}

void setWaterValve(int port, int state){
  if (state == 1)
    digitalWrite(port,HIGH);
  else 
    digitalWrite(port,LOW);
}

