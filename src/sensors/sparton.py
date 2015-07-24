'''

Sparton IMU

'''
from threading import Lock,Thread
import serial

class Sparton:
  def __init__(self,port):
    self.pitch = 0
    self.roll = 0
    self.yaw = 0
    self.lock = Lock()
    self.thread = Thread(target= self.loopMain, args=(port))
    self.thread.start()
  def loopMain(self,port):
    usb3 = serial.Serial(port,112500)
    usb3.write("1 compass.p\r\n")
    while True:
          printout = usb3.readline()
          splitprint = printout.split(",")
          if splitprint[0] == "C":
              try:
                  self.lock.acquire()
                  self.pitch = float(splitprint[2])
                  self.roll = float(splitprint[3])
                  self.yaw = float(splitprint[4])
              except ValueError, IndexError:
                  pass
              finally:
                  self.lock.release()


  # Return: roll, pitch, heading
  def read(self):
      self.lock.acquire()
      results = (self.pitch,self.roll,self.yaw)
      self.lock.release()
      return results
