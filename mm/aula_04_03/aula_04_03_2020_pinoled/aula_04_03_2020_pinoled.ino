int pinoLED = 8; // pinoLED é uma variável do pino selecionado, no caso, 8

void setup() {
  pinMode(pinoLED, OUTPUT); // inicializa o pino ledPin (porta 8) como um OUTPUT
}



void loop() {
  digitalWrite(pinoLED, HIGH); // liga o LED (HIGH = 5 V)
  delay(25); //espera 250 ms
  digitalWrite(pinoLED, LOW); //desliga o LED (LOW = 0 V)
  delay(50); //espera 500 ms
}

