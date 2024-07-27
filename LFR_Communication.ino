#include <WiFi.h>
#include <Wire.h>
// for left:"0,0,70,0"
//for right:"70,0,0,0"
const char *ssid = "device";
const char *password = "password";
const char *host = "0.0.0.0"; // Change this to the IP address of your Python server
const int port = 8080;

WiFiClient client;

// Define pin numbers for digital IR sensors
const int irSensorPins[5] = {13, 15, 27, 14, 12};

// Define pin numbers for motor control
const int leftMotorPin1 = 5;
const int leftMotorPin2 = 18;
const int rightMotorPin1 = 19;
const int rightMotorPin2 = 21;

void setup() {
  Serial.begin(115200);

  // Connect to WiFi
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi...");
  }
  Serial.println("Connected to WiFi");

  // Initialize motor control pins
  pinMode(leftMotorPin1, OUTPUT);
  pinMode(leftMotorPin2, OUTPUT);
  pinMode(rightMotorPin1, OUTPUT);
  pinMode(rightMotorPin2, OUTPUT);
}


void loop() {
  int irSensorValues[5];

  // Read sensor values
  for (int i = 0; i < 5; i++) {
    irSensorValues[i] = digitalRead(irSensorPins[i]);
  }

  // If not connected, attempt to reconnect
  if (!client.connected()) {
    if (!client.connect(host, port)) {
      Serial.println("Connection failed.");
      delay(1000);
      return;
    }
  }
  
  // Send IR sensor values as a string to Python server
  String sensorData = "";
  sensorData = sensorData + irSensorValues[0] + "," + irSensorValues[1] + "," + irSensorValues[2] + "," + irSensorValues[3] + "," + irSensorValues[4] + ",";
  client.println(sensorData);
  Serial.println("Sent: " + sensorData);

  // Receive motor control commands from Python
  while (client.available())
  {
    String command = client.readStringUntil('\n');
    command.trim();
    Serial.println("Received Command: " + command);
    int value[4];
    sscanf(command.c_str(), "%d,%d,%d,%d", &value[0], &value[1], &value[2], &value[3]);
    
    analogWrite(leftMotorPin1, value[0]);
    analogWrite(leftMotorPin2, value[1]);
    analogWrite(rightMotorPin1, value[2]);
    analogWrite(rightMotorPin2, value[3]);
  }
}

