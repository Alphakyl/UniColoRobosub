'''

Rudimentary PID Loops

'''

import time

class PIDLoop:
  def __init__(self, kP, kI, kD):
    self.kP, self.kI, self.kD = kP, kI, kD
    self.last_update, self.last_error, self.integral = None, None, 0.

  def __call__(self, actual, target):
    now = time.time()
    dt = now - self.last_update if self.last_update is not None else 0.

    self.error = target - actual

    self.derivative = (self.error - self.last_error) / dt if self.last_error is not None and dt > 0. else 0.

    self.integral += dt * self.error

    self.last_error = self.error
    self.last_update = now
    
    self.output = (self.kP * self.error) + (self.kI * self.integral) + (self.kD * self.derivative)

    # HACK: clamp output to -1 to 1 range
    if self.output < -1:
        self.output = -1
    elif self.output > 1:
        self.output = 1

    return self.output
