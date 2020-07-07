#include <Arduino.h>

int mq2 = A2;
int mq4 = A3;
int mq5 = A4;
int mq135 = A5;

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
  Serial.print(" ");
  Serial.println(reading);
}

void loop() {
  int mq2Reading = analogRead(mq2);
  int mq4Reading = analogRead(mq4);
  int mq5Reading = analogRead(mq5);
  int mq135Reading = analogRead(mq135);

  Serial.println("-");
  valuePrint("mq2", mq2Reading);
  valuePrint("mq4", mq4Reading);
  valuePrint("mq5", mq5Reading);
  valuePrint("mq135", mq135Reading);

  delay(1000);
}