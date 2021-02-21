#include <ESP8266WiFi.h>
#include <Ticker.h>

#define MAX_SRV_CLIENTS 3   //最大同时连接数，即你想要接入的设备数量，8266tcpserver只能接入五个，哎
WiFiServer server(8080);//你要的端口号，随意修改，范围0-65535
//WiFiClient serverClients[MAX_SRV_CLIENTS];
WiFiClient client;


const char *ssid     = "qinhh";//这里写入网络的ssid
const char *password = "58766730";//wifi密码

static const uint8_t LED_Red = 2;
static const uint8_t LED_Green = 2;
static const uint8_t LED_Reset = 3;

//static const uint8_t LED_Red = 12;
//static const uint8_t LED_Green = 4;
//static const uint8_t LED_Reset = 14;

#define bufferSize 8192
#define packTimeout 5 // ms (if nothing more on UART, then send packet)

uint8_t buf1[bufferSize];
uint16_t i1=0;

uint8_t buf2[bufferSize];
uint16_t i2=0;

Ticker flipper;
//Ticker flipper2;

bool show = false;

void flip()
{
  if (show) {
    show = false;
    digitalWrite(LED_Red, HIGH); //红灯
  }
  else
  {
    show = true;
    digitalWrite(LED_Red, LOW); //红灯
  }
}

void setup() {

  Serial.begin(115200);
  Serial.println();
  Serial.print("Connecting to ");
  Serial.println(ssid);


  pinMode(LED_Red, OUTPUT);
  pinMode(LED_Green, OUTPUT);

  flipper.attach(0.5, flip);//红灯闪动

  WiFi.begin(ssid, password);//启动

  //在这里检测是否成功连接到目标网络，未连接则阻塞。
  while (WiFi.status() != WL_CONNECTED)
  {
    delay(100);
  }

  //几句提示
  Serial.println("");
  Serial.println("WiFi connected");
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());

  server.begin();
  server.setNoDelay(true);  //加上后才正常些

  flipper.detach();


  //flipper2.attach(0.5,loop2);
  digitalWrite(LED_Red, LOW);//绿灯常亮
}


void loop() {
    if(!client.connected()) { // if client not connected
    client = server.available(); // wait for it to connect
    return;
  }

  // here we have a connected client

  if(client.available()) {
    while(client.available()) {
      buf1[i1] = (uint8_t)client.read(); // read char from client (RoboRemo app)
      if(i1<bufferSize-1) i1++;
    }
    // now send to UART:
    Serial.write(buf1, i1);
    i1 = 0;
  }

  if(Serial.available()) {
     char ch = (char)Serial.read();
     client.print(ch);
    

    // read the data until pause:
    
//    while(1) {
//      if(Serial.available()) {
//        buf2[i2] = (char)Serial.read(); // read char from UART
//        if(i2<bufferSize-1) i2++;
//      } else {
//        //delayMicroseconds(packTimeoutMicros);
//        delay(packTimeout);
//        if(!Serial.available()) {
//          break;
//        }
//      }
//    }
    
    // now send to WiFi:
//    client.write((char*)buf2, i2);
//    i2 = 0;
  }

  
}
