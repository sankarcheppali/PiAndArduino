#include "Arduino.h"
#include "SerialPublish.h"
#include "SoftwareSerial.h"

 SerialPublish::SerialPublish(int rx,int tx): _SoftSerial(rx, tx)
 {
      _SoftSerial.begin(9600);
     	i=0;
      inputString="";
      stringComplete=false;
      pIndex=0;
}
void SerialPublish::publish(String str,float *ptr)
 {
   s[pIndex]=str;
   p[pIndex]=ptr;
   pIndex++;
 }
 
 
void SerialPublish::sync()
{
    // _SoftSerial.println("Sync");
     serialEve();
    if (stringComplete) {
   // _SoftSerial.println("Got one request");
    for(i=0;i<pIndex;i++)
    {
       //check for =, if = is there then it is put request
       if(inputString.indexOf('=')==-1){ //this is a get request
        if(s[i].equalsIgnoreCase(inputString.substring(2,inputString.indexOf('>'))))
        {
         // _SoftSerial.print(inputString.substring(2,inputString.indexOf('>'))+":");
          _SoftSerial.println(*p[i]);
        }
    }
      else //this is a put request
      {
        if(s[i].equalsIgnoreCase(inputString.substring(2,inputString.indexOf('='))))
        {
          //_SoftSerial.print(inputString.substring(2,inputString.indexOf('='))+":");
          *p[i]=inputString.substring(inputString.indexOf('=')+1,inputString.indexOf('>')).toFloat();
           _SoftSerial.println(*p[i]);
        
        }
        
      }
      
    }
    //Serial.println(inputString);
    
    // clear the string:
    inputString = "";
    stringComplete = false;
  }
}

/*
  SerialEvent occurs whenever a new data comes in the
 hardware serial RX.  This routine is run between each
 time loop() runs, so using delay inside loop can delay
 response.  Multiple bytes of data may be available.
 */
void SerialPublish::serialEve() {
  while (_SoftSerial.available()&& !stringComplete) {
    // get the new byte:
    char inChar = (char)_SoftSerial.read();
    // add it to the inputString:
    inputString += inChar;
    // if the incoming character is a newline, set a flag
    // so the main loop can do something about it:
    if (inChar == '>') {
      stringComplete = true;
    }
  }
}


