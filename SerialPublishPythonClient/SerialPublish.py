#this program will create an object, for sending and receving the data
#from sensor node.
#the com port should be configurable
#baud rate is 9600bps
#getResource() takes variable name(string),returns a float
#setResource() takes variable name (string) and float value returns for success

import serial
import time
class SerialPublish:
    def __init__(self,com):
        self.ser=serial.Serial()
        self.ser.baudrate=9600
        self.ser.timeout=3
        self.ser.port=com
    def getResource(self,resource):
        try:
            self.ser.open()
            self.ser.write('<?'+resource+'>')
            return self.ser.readline()
        finally:
            self.ser.close()
    def setResource(self,resource,value):
        try:
            self.ser.open()
            self.ser.write('<?'+resource+'='+value+'>')
            return self.ser.readline()
        finally:
            self.ser.close()
