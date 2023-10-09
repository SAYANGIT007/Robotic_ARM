//HARE KRISHNA
#include <Wire.h>
#include <Adafruit_PWMServoDriver.h>
#include <cvzone.h>
#define servoMIN 95 // not used here
#define servoMAX 610 // not used here

SerialData data(3, 3); //(numOfValsRec,digitsPerValRec)
// From python : [handType,handpoint,pulsevalue]
Adafruit_PWMServoDriver arm = Adafruit_PWMServoDriver();
int valsRec[3]; // array of int with size numOfValsRec 


void setup() 
{
  data.begin(9600);
  arm.begin();
  arm.setPWMFreq(60);
}

void loop() 
{
  data.Get(valsRec);

  if(valsRec[0]==0 && valsRec[1]==8)// left hand. Two fingers up     // base servo(12)
  {
   arm.setPWM(12, 0, valsRec[2]); // 12 is servo pin 12 in motor driver
  }
  
  if(valsRec[0]==0 && valsRec[1]==12)// left hand. Three fingers up     // left servo(13)
  {
    arm.setPWM(13, 0, valsRec[2]); // 13 is servo pin 13 in motor driver
  }

  if(valsRec[0]==1 && valsRec[1]==8) // right hand. Two fingers up  // claw servo(8)
  {
   arm.setPWM(8, 0, valsRec[2]); // 8 is servo pin 8 in motor driver
  }

  if(valsRec[0]==1 && valsRec[1]==12)  // right hand. Three fingers up // right servo(15)
  {
   arm.setPWM(15, 0, valsRec[2]); // 15 is servo pin 15 in motor driver
  }
  

}
