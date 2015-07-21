'''

Control Configuration

Directions: X (forward), Y (sideways), Z (up/down).

Right-handed coordinate system (sub-relative): positive X ~ forward, positive Y ~ right, positive Z ~ up.

Right-handed coordinate system (global): X: north, Y: east, Z: depth (0 at surface; unchanged from sub-relative).

'''

class pid:
  class relative:
    kP_X, kI_X, kD_X = 0.1, 0., 0.
    kP_Y, kI_Y, kD_Y = 0.1, 0., 0.
    kP_Z, kI_Z, kD_Z = 0.1, 0., 0.

    kP_R, kI_R, kD_R = 0.1, 0., 0.
    kP_P, kI_P, kD_P = 0.1, 0., 0.
    kP_Y, kI_Y, kD_Y = 0.1, 0., 0.
