
#ifndef SERIAL_RATE
#define SERIAL_RATE         115200
//#define SERIAL_RATE         9600
#endif

#ifndef SERIAL_TIMEOUT
#define SERIAL_TIMEOUT      5
#endif
#include <MsTimer2.h>
#include <Wire.h> 
#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C lcd(0x27,16,2); // set the LCD address to 0x27 for a 16 chars and 2 line display

void setup() {
  Serial.begin(SERIAL_RATE);
  Serial.setTimeout(SERIAL_TIMEOUT);

  /*int cmd = readData();
    for (int i = 0; i < cmd; i++) {
      pinMode(readData(), OUTPUT);
    }*/
  //for (int i = 2; i < 9; i++)
  //  pinMode(i, OUTPUT);

  //pinMode(3, OUTPUT);
  //pinMode(13, OUTPUT);
  //digitalWrite(13, LOW);
  //digitalWrite(3, LOW);

// 中断设置函数，每 500ms 进入一次中断
   MsTimer2::set(5, event);
   //开始计时
   MsTimer2::start(); 

   lcd.init(); // initialize the lcd 
  lcd.backlight(); //Open the backlight
  lcd.print("xxxx "); // Print a message to the LCD.
  lcd.setCursor(0,1); //newline
  lcd.print("www.yfrobot.com");// Print a message to the LCD
}

int pwrite = 0;
int readpin[8]; //需要读的列表

void event()
{
    byte ret =0;

    //多个pin值，并入到一个值中
    int num = 0;
    for(int i =0; i < 8;i++){
      if (readpin[i] == 0)
        break;
      byte v = digitalRead(readpin[i]);
      ret = ret | (v << i);
      num++;
    }

    //Serial.println("xx");
    if (num >0)
      Serial.write(ret);

}

bool temp = false;

void loop() {
  byte v = readData2();
  if (v == 0) { //如果是0，则为测试信号
    Serial.write(0);
    return ;
  }

  lcd.setCursor(0,1); //newline
  lcd.print(v);// Print a message to the LCD

  byte cmd = v >> 6 ;  //头两个为命令类型
  byte param = (v & 0x30) >> 4; //高四位中后两位为命令参数
  char pin = v & 0x0F;  //低四位为pin编号

  //  Serial.write(v);
  //  Serial.write(cmd);
  //  Serial.write(param);
  //  Serial.write(pin);

  if (cmd == 0) { //设置PIN类型
    if (param == 1)
      pinMode(pin, OUTPUT);
    else if (param == 2)
      pinMode(pin, INPUT);
    else if (param == 3)
      pinMode(pin, INPUT_PULLUP);
  }
  else if (cmd == 1) { //写值
    if (param == 0)
      digitalWrite(pin, LOW);
    else if (param == 1)
      digitalWrite(pin, HIGH);
  }
  else if (cmd == 2) {//读值
    Serial.write(digitalRead(pin));
  }
  else if (cmd == 3) {//设置批量读值
    if (param == 0){
      pwrite = 0;
      for(int i =0;i < 8;i++)
        readpin[i] = 0; //清空所有
    }
    else if (param == 1){
      readpin[pwrite] = pin;
      pwrite = pwrite + 1;
    }
    //Serial.println(pwrite);
  }

  /*if (temp) {
    digitalWrite(3, LOW);
    digitalWrite(13, HIGH);
    temp = false;
  }
  else {
    digitalWrite(3, LOW);
    digitalWrite(13, LOW);
    temp = true;
  }*/
  //analogWrite
  //analogRead
}


byte readData2() {
  byte buffer [1];
  while (1) {
    if (Serial.available() > 0) {
      //char x = Serial.parseInt();
      Serial.readBytes(buffer, 1);
      return buffer[0];
    }
  }
}


char readData() {
  while (1) {
    if (Serial.available() > 0) {
      char x = Serial.parseInt();
      Serial.println("w");
      return x;
    }
  }
}
