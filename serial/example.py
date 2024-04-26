import serial



ser = serial.Serial()
ser.port = 'COM26'
ser.baudrate = '115200'
print(ser.name) 
ser.open()
ser.write("3".encode('utf-8'))
data=b'\n'
#data='2\n'
ser.write(data)
#ser.write(data.encode('utf-8'))

readdata=ser.read(1)
print(readdata.decode())
ser.close()