int pinoLED = 3;           // pino PWM que o LED está conectado
int brilho = 0;    // quantidade de brilho
int qntdeBrilho = 5;    //salto entre um estado de brilho e outro

void setup() { 
  pinMode(pinoLED, OUTPUT); // pino 3, que aceita PWM, como saída
}

void loop() {
  analogWrite(pinoLED, brilho); // joga na saída o brilho da saída 9
  brilho = brilho + qntdeBrilho; // incrementa o brilho da quantidade definidade
  if (brilho == 0 || brilho == 255) { 
    qntdeBrilho = - qntdeBrilho;  //quando eu chegar no máximo (255) ou no mínimo (0) eu inverto o sinal do incrmento
  }
  delay(30); // espera de 300 ms
}

