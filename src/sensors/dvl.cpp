#include "pd5Com.h"
#include <iostream>
#include <fstream>
#include <string>
#include <math.h>

#define DEPTH_OFFSET 0.7
#define TRANS_ANGLE 30 //22.5
#define ROTATION -45
#define deg_2_rad(a) (3.1415926*a/180)

void start(const string& port, std::ostream &output) {
    Pd5Com comm (port);
    dvl_pd5 packet;

    for(;;) {
        //read a new packet from DVL
        packet = comm.getData();
        
        if (packet.DVL_DATA_IDh != 0) {
            double velocity_x, velocity_y, velocity_z;
            velocity_x = (double)(packet.BTM_VEL.y)/1000.0;
            velocity_y = (double)(packet.BTM_VEL.x)/1000.0;
            velocity_z = (double)(packet.BTM_VEL.z)/1000.0;

            output << "DVL," << std::to_string(velocity_x) << "," << std::to_string(velocity_y) << "," << std::to_string(velocity_z) << std::endl;
        }
    }
}

int main(int argc, char* argv[]) {
    if (argc < 2) {
        std::cout << "Need dvl path" << std::endl;
    }

    if (mkfifo("/var/run/dvl", 0666)) {
        perror("fifo");
    }

    std::ofstream fifo("/var/run/dvl");
    start(argv[1], fifo);
}
