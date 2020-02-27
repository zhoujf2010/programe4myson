
#ifndef SERIAL_RATE
#define SERIAL_RATE         115200
//#define SERIAL_RATE         9600
#endif

#ifndef SERIAL_TIMEOUT
#define SERIAL_TIMEOUT      5
#endif

void setup() {
  Serial.begin(SERIAL_RATE);
  Serial.setTimeout(SERIAL_TIMEOUT);

  /*int cmd = readData();
    for (int i = 0; i < cmd; i++) {
      pinMode(readData(), OUTPUT);
    }*/
  for (int i = 2; i < 9; i++)
    pinMode(i, OUTPUT);
}

void loop() {
  byte v = readData2();
  if (v == 0) { //如果是0，则为测试信号
    Serial.write(0);
    return ;
  }


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
