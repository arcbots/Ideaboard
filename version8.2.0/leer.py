import time
import board
from digitalio import DigitalInOut, Direction, Pull
from ideaboard import IdeaBoard
from time import sleep
from adafruit_rtttl import play

# Digital Output on IO27
switch = DigitalInOut(board.IO27) # Choose pin 27
switch.direction = Direction.INPUT
ib = IdeaBoard()

while True:
    if switch.value:
        print("avanzar")
        ib.motor_1.throttle = 1.0
        ib.motor_2.throttle = -1.0
        time.sleep(0.1)
        song = "StarWars:d=4,o=5,b=45:32p,32f#,32f#,32f#,8b.,8f#.6,32e6,32d#6,32c#6,8b.6,16f#.6,32e6,32d#6,32c#6,8b.6,16f#.6,32e6,32d#6,32e6,8c#.6,32f#,32f#,32f#,8b.,8f#.6,32e6,32d#6,32c#6,8b.6,16f#.6,32e6,32d#6,32c#6,8b.6,16f#.6,32e6,32d#6,32e6,8c#6";
        play(board.IO25, song)
        time.sleep(0.1)
    else:
        print("Detenerse")
        ib.motor_1.throttle = 0
        ib.motor_2.throttle = 0
        time.sleep(0.1)
        song = "IronMan:d=4,o=5,b=155:2b4,2d5,4d5,4e5,2e5,8g5,8f#5,8g5,8f#5,8g5,8f#5,4d5,4d5,4e5,2e5"
        play(board.IO25, song)
    
    
        

