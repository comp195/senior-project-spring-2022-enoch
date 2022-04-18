#!/usr/bin/env python3
import serial
import time

if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyACM0',115200, timeout=1)
    ser.flush()
    
    while True:
        #ser.write(b"Forward\n")
        #time.sleep(1)
        ser.write(b"Backward\n")
        time.sleep(1)
        ser.write(b"Left\n")
        time.sleep(1)
        ser.write(b"Right\n")
        time.sleep(1)
        ser.write(b"EMO\n")
        time.sleep(1)
