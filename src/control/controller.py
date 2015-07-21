'''

Basic PID 6-DOF Controller

'''

from auxiliary.logging import mkLog, STANDARD, DEBUG, CRITICAL

log = mkLog('CONTROLLER')

from control.pid import PIDLoop
import control.config as config

class RelativeController:
  def __init__(self):
    self.pidX = PIDLoop(kP = config.pid.relative.kP_X, kI = config.pid.relative.kI_X, kD = config.pid.relative.kD_X)
    self.pidY = PIDLoop(kP = config.pid.relative.kP_Y, kI = config.pid.relative.kI_Y, kD = config.pid.relative.kD_Y)
    self.pidZ = PIDLoop(kP = config.pid.relative.kP_Z, kI = config.pid.relative.kI_Z, kD = config.pid.relative.kD_Z)

    self.pidR = PIDLoop(kP = config.pid.relative.kP_R, kI = config.pid.relative.kI_R, kD = config.pid.relative.kD_R)
    self.pidP = PIDLoop(kP = config.pid.relative.kP_P, kI = config.pid.relative.kI_P, kD = config.pid.relative.kD_P)
    self.pidQ = PIDLoop(kP = config.pid.relative.kP_Y, kI = config.pid.relative.kI_Y, kD = config.pid.relative.kD_Y)

  def run(self, dxT, dxA, dyT, dyA, zT, zA, rT, rA, pT, pA, qT, qA):
    xO, yO, zO = self.pidX(dxA, dxT), self.pidY(dyA, dyT), self.pidZ(zA, zT)
    rO, pO, qO = self.pidR(rA, rT), self.pidP(pA, pT), self.pidQ(qA, qT)

    log('Target (dX/dY/Z R/P/Y): {0}/{1}/{2} {3}/{4}/{5}'.format(dxT, dyT, zT, rT, pT, qT), DEBUG)
    log('Actual (dX/dY/Z R/P/Y): {0}/{1}/{2} {3}/{4}/{5}'.format(dxA, dyA, zA, rA, pA, qA), DEBUG)
    log('Output (dX/dY/Z R/P/Y): {0}/{1}/{2} {3}/{4}/{5}'.format(xO, yO, zO, rO, pO, qO), DEBUG)  
