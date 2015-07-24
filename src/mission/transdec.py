#!/usr/bin/env python3.4

'''

Main TRANSDEC Mission

'''

import time
from control.controller import RelativeController
from auxiliary.logging import mkLog, DEBUG, STANDARD, CRITICAL

log = mkLog('MISSION')

from mission.framework import *

def run():
  controller = RelativeController()
  time.sleep(5)
  (p,r,initialHeading) = controller.sparton.read()
  for i in range(10):
      controller.step(0,0,-5,0,0,initialHeading)
      time.sleep(.1)
  while True:
      controller.step(50,0,-5,0,0,initialHeading)
  
if __name__ == '__main__':
  run()
