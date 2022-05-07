#!/usr/bin/env python3
import serial
import time
import keyboard

if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyACM0',115200, timeout=1)
    ser.flush()

while True:
        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN and event.name == 't':
                print('t was pressed\n')
                ser.write(b"t\n")
        elif event.event_type == keyboard.KEY_DOWN and event.name == 'a':
                print('a was pressed\n')
                ser.write(b"a\n")
        elif event.event_type == keyboard.KEY_DOWN and event.name == 's':
                print('s was pressed\n')
                ser.write(b"s\n")
        elif event.event_type == keyboard.KEY_DOWN and event.name == 'd':
                print('d was pressed\n')
                ser.write(b"d\n")
        elif event.event_type == keyboard.KEY_DOWN and event.name == 'f':
                print('f was pressed\n')
                ser.write(b"f\n")
        elif event.event_type == keyboard.KEY_DOWN and event.name == 'w':
                print('w was pressed\n')
                ser.write(b"w\n")
        elif event.event_type == keyboard.KEY_DOWN and event.name == 'e':
                print('e was pressed\n')
                ser.write(b"e\n")
        elif event.event_type == keyboard.KEY_DOWN and event.name == 'r':
                print('r was pressed\n')
                ser.write(b"r\n")
        elif event.event_type == keyboard.KEY_DOWN and event.name == 'i':
                print('i was pressed\n')
                ser.write(b"i\n")
        elif event.event_type == keyboard.KEY_DOWN and event.name == 'j':
                print('j was pressed\n')
                ser.write(b"j\n")
        elif event.event_type == keyboard.KEY_DOWN and event.name == 'm':
                print('m was pressed\n')
                ser.write(b"m\n")
        elif event.event_type == keyboard.KEY_DOWN and event.name == 'k':
                print('k was pressed\n')
                ser.write(b"k\n")
        elif event.event_type == keyboard.KEY_DOWN and event.name == 'p':
                print('quit was pressed\n')
                quit()

"""
def show():
    #show key
    
    while True:
        while True:
            cheese = keyboard.read_key()
            if keyboard != "":
                if cheese == 'a': 
                    print("\nyou pressed A")
                    ser.write(b"Backward\n")
                    break
                #counter = counter - 1
                #print(counter)
                #time.sleep(10)
                elif cheese == 'b': 
                    print("\nyou pressed B")
                    ser.write(b"Right\n")
                    break
            else:
                break
    #print(keyboard.read_key())
    #print(cheese)
    #reset show()
    #if keyboard !="":
    #    time.sleep(0.1)
    #    show()
#start
show()
"""
"""
def on_press(key):
	if key.char == 'a': 
		print("\nyou pressed A")
		ser.write(b"Backward\n")
	elif key.char == 'b': 
		print("\nyou pressed B")
		ser.write(b"Right\n")
	elif key.char == 'c': 
		print("\nyou pressed C")
		ser.write(b"Left\n")
	elif key.char == 'd': 
		print("\nyou pressed D")
		ser.write(b"Right\n")
with keyboard.Listener(on_press=on_press) as listener:
	listener.join()

"""

"""
while True:
    
    if keyboard.press(key) != ("a"):
        print("error")

        if keyboard.press("q"):
            ser.write(b"Backward\n")
            #    ser.write(b"Backward\n")
            #    print("You pressed q")
            #    break
        elif keyboard.press("w"):
            #if True:
            #    print("You pressed w")
            ser.write(b"Left\n")
            #    break
            #ser.write(b"Right\n")
            #time.sleep(1)
            #ser.write(b"Backward\n")
            
            #time.sleep(1)
            #ser.write(b"Left\n")
            #time.sleep(1)
            #ser.write(b"Right\n")
            #time.sleep(1)
            #ser.write(b"EMO\n")
            #time.sleep(1)
            """