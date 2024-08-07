void setup() {
  Serial.begin(115200);
}

void loop() {
  int x_axis = analogRead(A0);
  int y_axis = analogRead(A1);
  
  Serial.print("X:");
  Serial.print(x_axis);
  Serial.print(",Y:");
  Serial.println(y_axis);
  
  delay(100);
}
