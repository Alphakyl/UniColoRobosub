'''

DVL Interface

'''

from threading import Lock,Thread
import serial

class DVL:
  def __init__(self):
    virtualFile = open("/var/run/dvl")
    self.lock = Lock()
    self.thread = Thread(self.loopMain)
    self.thread.start()
  def loopMain(self):
      for line in self.virtualFile:
          splitline = line.split(",")
          if splitline[0] == "DVL":
              try:
                  self.lock.acquire()
                  self.xVelocity = float(splitline[1])
                  self.yVelocity = float(splitline[2])
                  self.zVelocity = float(splitline[3])
              except ValueError,IndexError:
                  pass
              finally:
                  self.lock.release()



  # Return velx, vely
  def read(self):
      self.lock.acquire()
      results = (self.xVelocity,self.yVelocity,self.zVelocity)
      self.lock.release()
      return results
