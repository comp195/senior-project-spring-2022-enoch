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

#print("variables passed test 1")

#note by default we will test that all movement options are working

###########

#move up
def up():
	print("now testing upward movement")
	LM2.on()
	RM2.on()

#move down
def down():
	print("now testing downward movement")
	LM1.on()
	RM1.on()

#move left
def left():
	print("now testing left movement")
	RM2.on()

#move right
def right():
	print("now testing right movement")
	LM2.on()

#move up
def stop():
	LM1.off()
	RM1.off()
	LM2.off()
	RM2.off()

###########

# test 1 making sure that state UP is working
def test_up():
	print("now testing upward movement")
	LM2.on()
	RM2.on()
	
	print("running...")
	time.sleep(3)

	LM2.off()
	RM2.off()
	print("upward movement test concluded")

def test_down():
	print("now testing downward movement")
	LM1.on()
	RM1.on()
	print("running...")
	time.sleep(3)

	LM1.on()
	RM1.on()
	print("downward movement test concluded")

def test_left():
	print("now testing left movement")
	RM2.on()
	print("running...")
	time.sleep(3)

	RM2.off()
	print("left movement test concluded")

def test():
    print("peaches")

def test_right():
	print("now testing right movement")
	LM2.on()
	print("running...")
	time.sleep(3)

	LM2.off()
	print("right movement test concluded")

test_up()
#test_down()
#test_left()
#test_right()
