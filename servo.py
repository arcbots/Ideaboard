import board
from ideaboard import IdeaBoard
from time import sleep

ib = IdeaBoard()

servo1 = ib.Servo(board.IO4)

while True:
    servo1.angle = 0
    sleep(2)
    servo1.angle = 180
    sleep(2)


















