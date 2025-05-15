
from time import sleep
from ideaboard import IdeaBoard
import board

ib = IdeaBoard()

led = ib.led(board.I034)


while True:
    led.on()
    sleep(0.001)
    led.off()
    sleep(0.001)