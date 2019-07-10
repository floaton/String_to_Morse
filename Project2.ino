/*
 * Code to blink an LED using Python
 * Code by: Aswint Raj, Dated: 8-9-2017
 * Webiste: www.circuitdigest.com
 */

int data;
int k;
void setup() { 
  Serial.begin(9600); //initialize serial COM at 9600 baudrate
  pinMode(LED_BUILTIN, OUTPUT); //make the LED pin (13) as output
  analogWrite (LED_BUILTIN, 0);
  
  Serial.println("Hi!, I am Arduino");
}
void loop() {
analogWrite(LED_BUILTIN, 0);
delay(1000);
k=0;
if (k%5==0){
  delay(2000);
}
data = Serial.read(); 
    if (data == '1'){
      analogWrite (LED_BUILTIN, 5);
      delay(10000);
      k=k+1;
    }
    else if (data == '3'){
      analogWrite (LED_BUILTIN, 5);
      delay(3000);
      k=k+1;
    }
    else if (data == '5'){
      analogWrite (LED_BUILTIN, 0);
      delay(6000);
      k=k+1;
    }
    else if (data == '0'){
      analogWrite (LED_BUILTIN, 0);
      delay(1);
      k=k+1;
    }
}
