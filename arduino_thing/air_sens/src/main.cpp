#include <Arduino.h>

int mq2 = A2;
int mq4 = A3;
int mq5 = A4;
int mq135 = A5;
int incomingByte;

void setup() {
  pinMode(mq2, INPUT);
  pinMode(mq4, INPUT);
  pinMode(mq5, INPUT);
  pinMode(mq135, INPUT);
  Serial.begin(9600);
}

/* valuePrint prints the value for this label.
 *  Creates side effects only.
 */
void valuePrint(String label, int reading) {
  Serial.print(label);
  Serial.print("=");
  Serial.print(reading);
}

void loop() {
  // see if there's incoming serial data:
  if (Serial.available() > 0) {
    // read the oldest byte in the serial buffer:
    // "When you call Serial.read a byte is removed from the receive buffer and returned to your code"
    incomingByte = Serial.read();
    // if it's a capital H (ASCII 72), read the values and send them to the raspberry host.
    // TODO: ensure the message is always the same length, each time
    if (incomingByte == 72) {
      int mq2Reading = analogRead(mq2);
      int mq4Reading = analogRead(mq4);
      int mq5Reading = analogRead(mq5);
      int mq135Reading = analogRead(mq135);
      
      Serial.print("?");
      valuePrint("mq2", mq2Reading);
      Serial.print("&");
      valuePrint("mq4", mq4Reading);
      Serial.print("&");
      valuePrint("mq5", mq5Reading);
      Serial.print("&");
      valuePrint("mq135", mq135Reading);
      Serial.print("\n");
    }
  }
  // read the serial only every second
  delay(1000);
}