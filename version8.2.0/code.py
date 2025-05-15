from ideaboard import IdeaBoard
from time import sleep
import board

ib = IdeaBoard()


# motor speed is from -1.0 (reverse) to 1.0 (forward)
# 0 is stopped with brake, None = roll freel


while True:
    for i in range(256):
        ib.arcoiris = i
        sleep(0.01)
        if(i < 128):
            ib.motor_1.throttle = 1.0
            ib.motor_2.throttle = -1.0
        if(i >= 128):
            ib.motor_1.throttle = 0
            ib.motor_2.throttle = 0  
        
        
        
      
  
        

        
        
