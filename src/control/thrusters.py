import serial, time

chr = lambda x: bytes([x])

ser = serial.Serial('/dev/ttyACM0')
ser.write(chr(0xAA))
ser.flush()

def mset(channel, target):
  raw = chr(0x84) + chr(channel) + chr(target & 0x7F) + chr((target >> 7) & 0x7F)
  ser.write(raw)
