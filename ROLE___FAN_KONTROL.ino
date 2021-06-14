// -----FAN KONTROL BÖLÜMÜ

const int fan_in1 = 11;
const int fan_in2 = 10;
const int fan_in3 = 9;
const int fan_in4 = 8;

//ROLE VE SICAKLIK ÖLÇÜM__
int lm35Pin = A0;
#define relay 3
int zaman = 5000;  // 30 SANİYE OLARAK AYARLI 
int okunan_deger = 0 ;
float sicaklik_gerilim = 0 ;
float sicaklik = 0 ;

void setup() {
//ROLE KONTROL
Serial.begin(9600);
pinMode(relay,OUTPUT);



//FAN KONTROL
pinMode(fan_in1 , OUTPUT) ;
pinMode(fan_in2 , OUTPUT) ;
pinMode(fan_in3 , OUTPUT) ;
pinMode(fan_in4 , OUTPUT) ;

//delay(7200000); //   2 SAATTE BİR ÇALIŞMA SAĞLAYACAK ŞEKİLDE AYARLI ---- 
                //    DÖNGÜNÜN TAMAMINI 2 SAATE ALABİLİR----DİKKAT ET--- EĞER BURDA OLMAZ İSE DÖNGÜNÜN SONUNA AL YADA BU SÜREYİ KISALT--




  

}

void loop() {
okunan_deger = analogRead(lm35Pin);
sicaklik_gerilim = (5000.0/1023.0) * okunan_deger;
sicaklik  =sicaklik_gerilim / 10;
Serial.println(sicaklik);


  if(sicaklik <= 35){
    digitalWrite(relay,LOW);
    digitalWrite(fan_in3,LOW);
    digitalWrite(fan_in4,LOW);
  }
  else if(sicaklik >= 38){
    digitalWrite(relay,HIGH);
    digitalWrite(fan_in3,LOW);
    digitalWrite(fan_in4,HIGH);
    
  }

 
  delay(zaman);
  }
