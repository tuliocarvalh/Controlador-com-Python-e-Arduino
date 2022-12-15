
int button = 2;
int button2 = 3;
int button3 = 4;
int button4 = 5;

void setup() {
{
  Serial.begin(9600);
  pinMode(button, INPUT_PULLUP);
  pinMode(button2, INPUT_PULLUP);
  pinMode(button3, INPUT_PULLUP);
  pinMode(button4, INPUT_PULLUP);
  Serial.println("Starting...");
  
}
}
void loop(){


{
  if (digitalRead(button) == LOW)
  {
    Serial.println("button1");
    delay(100);
  }
}
{
    if (digitalRead(button2) == LOW) // Se o botão for pressionado
  {
    Serial.println("button2");
    delay(100);
  }
}
{
    if (digitalRead(button3) == LOW) // Se o botão for pressionado
  {
    Serial.println("button3");
    delay(100);
  }
}
{
    if (digitalRead(button4) == LOW) // Se o botão for pressionado
  {
    Serial.println("button4");
    delay(100);
  }
}
}