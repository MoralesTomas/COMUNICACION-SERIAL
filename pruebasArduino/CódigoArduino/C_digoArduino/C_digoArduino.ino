#include <Separador.h>

const int s7 = 7;
const int s8 = 8;
const int s9 = 9;
const int s10 = 10;
const int s11 = 11;
const int s12 = 12;
const int s13 = 13;

String cadena = "";
String r1 = "";
String r2 = "";
String r3 = "";
String r4 = "";
String r5 = "";
String rSeis = "";

Separador s;

void setup()
{
  pinMode(s7,OUTPUT);
  pinMode(s8, OUTPUT);
  pinMode(s9, OUTPUT);
  pinMode(s10, OUTPUT);
  pinMode(s11, OUTPUT);
  pinMode(s12, OUTPUT);
  pinMode(s13, OUTPUT);
  
  Serial.begin(9600);
  Serial.println("Conexión Establecida");
}

void loop(){
  
  while(Serial.available())
  {
    reiniciar();
    cadena = Serial.readString();
    cadena.replace("\n", "");
    Serial.println("La cadena leida es: "+cadena);
    r1 =  s.separa(cadena,',',0);

    if(r1 == "0"){
      Serial.println("Es para el tablero del jugador 1");
      digitalWrite (s8, HIGH);
      r2 =  s.separa(cadena,',',1);
      r3 =  s.separa(cadena,',',2);
      r4 =  s.separa(cadena,',',3);
      r5 =  s.separa(cadena,',',4);
      rSeis =  s.separa(cadena,',',5);
      Serial.println("R2:"+r2);
      Serial.println("R3:"+r3);
      Serial.println("R4:"+r4);
      Serial.println("R5:"+r5);
      Serial.println("R6:"+rSeis+"comprobando");
      
      if(r2 == "1"){
        Serial.println("aca1");
        digitalWrite (s13, HIGH);
      }
      else{
        digitalWrite (s13, LOW);
      }
      Serial.println("aca2");
      if(r3 == "1"){
        digitalWrite (s12, HIGH);
      }
      else{
        digitalWrite (s12, LOW);
      }
      Serial.println("aca3");
      if(r4 == "1"){
        digitalWrite (s11, HIGH);
      }
      else{
        digitalWrite (s11, LOW);
      }
      Serial.println("aca4");
      if(r5 == "1"){
        digitalWrite (s10, HIGH);
      }
      else{
        digitalWrite (s10, LOW);
      }
      Serial.println("aca5");
      if(rSeis == "1"){
        digitalWrite (s9, HIGH);
      }
      else{
        digitalWrite (s9, LOW);
      }
      
    }
    
    else if(r1 == "1"){
    digitalWrite (s7, HIGH);
    r2 =  s.separa(cadena,',',1);
    r3 =  s.separa(cadena,',',2);
    r4 =  s.separa(cadena,',',3);
    r5 =  s.separa(cadena,',',4);
    if(r2 == "1"){
        Serial.println("aca1");
        digitalWrite (s13, HIGH);
      }
      else{
        digitalWrite (s13, LOW);
      }
      Serial.println("aca2");
      if(r3 == "1"){
        digitalWrite (s12, HIGH);
      }
      else{
        digitalWrite (s12, LOW);
      }

      if(r4 == "1"){
        Serial.println("aca1");
        digitalWrite (s10, HIGH);
      }
      else{
        digitalWrite (s10, LOW);
      }
      Serial.println("aca2");
      if(r5 == "1"){
        digitalWrite (s9, HIGH);
      }
      else{
        digitalWrite (s9, LOW);
      }
    }
  }
  
  
}

void reiniciar(){
  digitalWrite (s7, LOW);
  digitalWrite (s8, LOW);
  digitalWrite (s9, LOW);
  digitalWrite (s10, LOW);
  digitalWrite (s11, LOW);
  digitalWrite (s12, LOW);
  digitalWrite (s13, LOW);
  
}
