import time
import board
from analogio import AnalogIn

# Connect potentiometer to pin 33
pot = AnalogIn(board.IO33)

while True:
    # Values are from 0 to 65535 (2 ** 16)
    print(pot.value)
    time.sleep(0.1)