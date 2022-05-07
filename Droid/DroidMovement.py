#!/usr/bin/env python3

import keyboard
import serial
from gpiozero import LED
import time

####left motors####
#IN1
LM1 = LED(12)
#IN2
LM2 = LED(13)

####right motors###
#IN3
RM1 = LED(19)
#IN4
RM2 = LED(26)

#move up
def up():
	LM2.on()
	RM2.on()

#move down
def down():
	LM1.on()
	RM1.on()

#move left
def left():
	RM2.on()

#move right
def right():
	LM2.on()

#move up
def stop():
	LM1.off()
	RM1.off()
	LM2.off()
	RM2.off()

while True:
	ser = serial.Serial('/dev/ttyACM0', 115200, timeout = 1)
	#ser.reset_input_buffer()
	if ser.in_waiting > 8:
		LM2.on()
		RM2.on()
	elif ser.in_waiting > 9:
		LM1.on()
		RM1.on()
	elif ser.in_waiting > 10:
		RM2.on()
	elif ser.in_waiting > 11:
		LM2.on()
	elif ser.in_waiting > 0:
		LM1.off()
		RM1.off()
		LM2.off()
		RM2.off()

