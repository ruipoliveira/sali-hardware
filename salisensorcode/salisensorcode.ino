

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);

}

int port_luminosity = 5;
int port_temperature = 2; 

void loop() {
  // put your main code here, to run repeatedly:
  //Serial.println(readTemperature(port_temperature));
  Serial.println("fsdfds"); 
  
  delay(60);        // delay in between reads for stability
  
}

int readTemperature(int port){
  int value = analogRead(port);

  return value;
}

int readLuminosity(int port){
  int value = analogRead(port);

  return value;
}

int readLiquidLevel(int x, int y){
  int result;
  result = x * y;
  return result;
}

int readSoilMoisture(int x, int y){
  int result;
  result = x * y;
  return result;
}
