import serial
import time

serialPort = serial.serial(
    port="COM26", baudrate=9600, bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE
)
serialString = ""  # Used to hold data coming over UART
while 1:
    # Read data out of the buffer until a carraige return / new line is found
    serialString = serialPort.readline()
    serialPort.sendline("HELLO\n")
    # Print the contents of the serial data
    try:
        print(serialString.decode("Ascii"))
    except:
        pass
    #nada

    