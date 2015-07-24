import serial, time

chr = lambda x: bytes([x])

ser = serial.Serial('/dev/ttyACM0')
ser.write(chr(0xAA))
ser.flush()
bud=chr(0x80)+chr(0x01)+chr(0x01)+chr(1)+chr(255)
bud1=chr(0x80)+chr(0x01)+chr(0x01)+chr(3)+chr(255)
bud2=chr(0x80)+chr(0x01)+chr(0x01)+chr(2)+chr(150)
bud3=chr(0x80)+chr(0x01)+chr(0x01)+chr(5)+chr(150)
bud4=chr(0x80)+chr(0x01)+chr(0x01)+chr(6)+chr(150)
bud5=chr(0x80)+chr(0x01)+chr(0x01)+chr(7)+chr(150)
ser.write(bud , bud1 , bud2 , bud3 , bud4 , bud5)
