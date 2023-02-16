import sys
import glob
import serial
import time
option='COM'


def serial_ports():
    """ Lists serial port names

        :raises EnvironmentError:
            On unsupported or unknown platforms
        :returns:
            A list of the serial ports available on the system
    """
    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        # this excludes your current terminal "/dev/tty"
        ports = glob.glob('/dev/tty[A-Za-z]*')
    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.*')
    else:
        raise EnvironmentError('Unsupported platform')

    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result


if __name__ == '__main__':
    print(serial_ports())
    option=raw_input("select port: ")
    print(option)
    ser = serial.Serial(option, 9600, timeout=0)
    #print(ser.readline())#L
    #print(ser.readline())#I
    #print(ser.readline())#N
    #print(ser.readline())#K
    #print(ser.readline())#
    #print(ser.readline())#S
    #print(ser.readline())#T
    #print(ser.readline())#A
    #print(ser.readline())#R
    #print(ser.readline())#T
    #ser.write('A')
    #ser.write('C')
    #ser.write('T')
    while(1):

        data=ser.readline()
        #print(data)
        #print(ord((data)))
        if(data=='A'):
            data=ser.readline()
            print(data)
            dataH=ord(data)
            data=ser.readline()
            print(data)
            dataL=ord(data)
            dato=(dataH<<8)|(dataL)
            print("DIstancia: %S" ((str)(dato/58)))
            time.sleep(1)
"""
http://petrimaki.com/2013/04/28/reading-arduino-serial-ports-in-windows-7/
http://stackoverflow.com/questions/12090503/listing-available-com-ports-with-python
https://joseguerreroa.wordpress.com/2012/06/28/manejo-de-arrays-y-matrices-en-python/

"""
