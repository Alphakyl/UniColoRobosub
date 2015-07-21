//
// Created by josh on 4/24/15.
//
#include <iostream>
#include "main.h"
#include "PID.h"

using namespace std;

int main()
{
    int x_error = 0;
    int time = 0;
    int commanded_throttle = pid(x_error, time);
    return 0;
}