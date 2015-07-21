#include "PID.h"

int pid(int error, int time)
{
  //Timer
  int timer = 0;
  int previous_time = 0;
  int previous_error = 0;

  //Calculate Delta t
  int current_time = (time - timer);
  int delta_t = current_time - previous_time;
  previous_time = current_time;

  //Calculate Integrator Error
  int I_error = I_error + error*delta_t;
  
  //Calculate Derivative Error
  int D_error = (error-previous_error)/delta_t;
  previous_error = error;
  
  return ((error * KP) + (I_error * KI) + (D_error * KD));
}



  
  