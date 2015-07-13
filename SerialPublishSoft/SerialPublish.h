#ifndef SerialPublish_h
#define SerialPublish_h
#include "Arduino.h"
#include <SoftwareSerial.h>


class SerialPublish
{
public:
	SerialPublish(int rx,int tx);
	void publish(String str,float *ptr);
	void sync();
	void serialEve();
private:
	float *p[20];//pointers to variables
    String s[20];//string(variable name)
    String inputString;         // a string to hold incoming data
    boolean stringComplete ;  // whether the string is complete
    int i;
    byte pIndex;//publisher index 
    SoftwareSerial _SoftSerial;   
};
#endif