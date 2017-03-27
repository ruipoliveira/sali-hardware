void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);

}

void loop() {
  // put your main code here, to run repeatedly:
  Serial.println("das");
  delay(1);        // delay in between reads for stability
  
}

int readTemperature(int x, int y){
  int result;
  result = x * y;
  return result;
}

int readLuminosity(int x, int y){
  int result;
  result = x * y;
  return result;
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
