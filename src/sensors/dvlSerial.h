#ifndef DVLSERIAL_H
#define DVLSERIAL_H

#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <termios.h>
#include <errno.h>
    
//max number of times we try to send data when writing over the serial port
#define MAX_RETRIES 255

class DVLSerialPort {
    public:
        DVLSerialPort(const char* devname);
        ~DVLSerialPort();

        //write the contents of buf to the serial port.
        //buf is size bytes long.  Returns 0 on success
        int writeSer(const unsigned char* buf, ssize_t size);

        //sends a break
        int sendBreak(int duration);

        //read maxSize bytes from the serial port, place in buf.
        //Returns 0 on success
	//now deprecated for most situations, unless infinite blocking is desired.  There is probably a better way to get that behavior too. -Tommy
	int readSer(unsigned char* buf, size_t size);
        
	//read up to maxSize bytes into buf
	//returns after uwait microseconds whether or not any bytes have been received 
	//Returns the number of bytes read, or -1 on error
	//Is there a more efficient way to get timeout behavior here besides select?  do we care? -Tommy
	ssize_t readWithTimeout(unsigned char *buf, size_t maxSize, long uwait);

	//attempt to read toRead bytes into buf within uwait microseconds
	//Returns the number of bytes actually read, or -1 on error
	//note: failing to read toRead bytes is not an error
	ssize_t readnWithTimeout(unsigned char *buf, size_t toRead, long uwait);	

	//flush in and out buffers.
	//Returns the return value of tcflush (0 on success)
	//I think the function only signals to the kernel to flush the buffers, so extra checking beyond the return value is probably in order if we want to be really really safe. -Tommy
	int flushBuffers();

	//flush only the input buffer
	int flushInput();
    private:
        int fd;
};

#endif
