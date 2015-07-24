'''

Basic PID 6-DOF Controller

'''

from auxiliary.logging import mkLog, STANDARD, DEBUG, CRITICAL

log = mkLog('CONTROLLER')

from control.pid import PIDLoop
import control.config as config

from sensors.dvl import DVL 
from sensors.sparton import Sparton

import numpy as np

class RelativeController:
  def __init__(self):
    self.pidX = PIDLoop(kP = config.pid.relative.kP_X, kI = config.pid.relative.kI_X, kD = config.pid.relative.kD_X)
    self.pidY = PIDLoop(kP = config.pid.relative.kP_Y, kI = config.pid.relative.kI_Y, kD = config.pid.relative.kD_Y)
    self.pidZ = PIDLoop(kP = config.pid.relative.kP_Z, kI = config.pid.relative.kI_Z, kD = config.pid.relative.kD_Z)

    self.pidR = PIDLoop(kP = config.pid.relative.kP_R, kI = config.pid.relative.kI_R, kD = config.pid.relative.kD_R)
    self.pidP = PIDLoop(kP = config.pid.relative.kP_P, kI = config.pid.relative.kI_P, kD = config.pid.relative.kD_P)
    self.pidQ = PIDLoop(kP = config.pid.relative.kP_Y, kI = config.pid.relative.kI_Y, kD = config.pid.relative.kD_Y)

    self.sparton = Sparton("/dev/ttyUSB0")
    self.dvl = DVL()

    # Each column is a thruster, each row a force
    # order: port starboard fp ap as fs sf sa
    #   x
    #   y
    #   z
    #   r
    #   p
    #   q
    self.thrust_mat = np.matrix(
            [[0.75, 0.75, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0.75, 0.75],
             [0, 0, 0.33, 0.33, 0.33, 0.33, 0, 0],
             [0, 0, 0.33, 0.33, -0.33, -0.33, 0, 0],
             [0, 0, 0.33, -0.33, -0.33, 0.33, 0, 0],
             [-0.25, 0.25, 0, 0, 0, 0, 0.25, -0.25]])

  def step(self, xvel, yvel, depth, pitch, roll, yaw):
    (xA, yA, zA) = self.dvl.read()
    (pA, rA, qA) = self.sparton.read()
    xO, yO, zO = self.pidX(xA, xvel), self.pidY(yA, yvel), self.pidZ(zA, depth)
    rO, pO, qO = self.pidR(rA, roll), self.pidP(pA, pitch), self.pidQ(qA, yaw)

    thrust_vec = np.matrix([xO, yO, zO, rO, pO, qO])
    thrust_out = thrust_vec * self.thrust_mat

    # TODO: take values from thrust_out and write them to thrusters
