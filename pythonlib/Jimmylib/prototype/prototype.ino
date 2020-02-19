
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
}

void loop() {
    switch (readData()) {
//        case -1 :
//            //测试信号
//            Serial.println("t");
        case 0 :
            //set digital low
            digitalWrite(readData(), LOW); break;
        case 1 :
            //set digital high
            digitalWrite(readData(), HIGH); break;
        case 2 :
            //get digital value
            Serial.println(digitalRead(readData())); break;
        case 3 :
            // set analog value
            analogWrite(readData(), readData()); break;
        case 4 :
            //read analog value
            Serial.println(analogRead(readData())); break;
        case 6 :
            pinMode(readData(), OUTPUT); break;
        case 7 :
            pinMode(readData(), INPUT); break;
        case 8 :
            pinMode(readData(), INPUT_PULLUP); break;
        case 99:
            //just dummy to cancel the current read, needed to prevent lock 
            //when the PC side dropped the "w" that we sent
            break;
    }
}

char readData() {
    while(1) {
        if(Serial.available() > 0) {
            char x = Serial.parseInt();
          Serial.println("w");
          return x;
        }
    }
}
