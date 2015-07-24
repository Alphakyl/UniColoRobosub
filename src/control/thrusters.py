import serial, time

chr = lambda x: bytearray([x])

ser = serial.Serial('/dev/ttyACM0')
# ser.baudrate = 9600
ser.write(chr(0xAA))
ser.flush()

MIN, MAX = 21, 234

inR = lambda x: max(0, min(256, x))

# Remap -1 to 1.

def mset(channel, target):
  raw = chr(0xFF) + chr(channel) + chr(inR(MIN + int(round((MAX - MIN) * (1 + target) / 2))))
  ser.write(raw)
  ser.flush()
