#this program will create an object, for sending and receving the data
#from sensor node.
#the com port should be configurable
#baud rate is 9600bps
#getResource() takes variable name(string),returns a float
#setResource() takes variable name (string) and float value returns for success

import serial
import time
class blueNode:
    def __init__(self,com):
        self.ser=serial.Serial()
        self.ser.baudrate=9600
        self.ser.timeout=3
        self.ser.port=com
        self.ser.open()
	self.msg=''
	self.oldMsg='Wellcome'
    def getResource(self,resource):
        try:
            self.ser.write('\r'+resource+'\n')
	    self.msg=self.ser.readline()
            if self.msg=='' or self.msg==None:
		self.msg=self.oldMsg
	    else:
		self.oldMsg=self.msg
	    return self.msg

        except:
		try:
            		self.ser.close()
	    		self.ser.open()
		except:
			self.ser.open()
			self.ser.inWaiting()
	
    
