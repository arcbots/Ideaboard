# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import time
import board
import adafruit_dht
from ideaboard import IdeaBoard
from ideaboard import IdeaBoard
from time import sleep


# ib.acroiris(0-255) creates a color wheel
# from 0 (RED) to 255 (RED


ib = IdeaBoard()

# motor speed is from -1.0 (reverse) to 1.0 (forward)
# 0 is stopped with brake, None = roll freely


# Initial the dht device, with data pin connected to:
dhtDevice = adafruit_dht.DHT11(board.IO26)

# you can pass DHT22 use_pulseio=False if you wouldn't like to use pulseio.
# This may be necessary on a Linux single board computer like the Raspberry Pi,
# but it will not work in CircuitPython.
# dhtDevice = adafruit_dht.DHT22(board.D18, use_pulseio=False)

while True:
    try:
        # Print the values to the serial port
        temperature_c = dhtDevice.temperature
        temperature_f = temperature_c * (9 / 5) + 32
        humidity = dhtDevice.humidity
        print(
            "Temp: {:.1f} F / {:.1f} C    Humidity: {}% ".format(
                temperature_f, temperature_c, humidity
            )
        )

    except RuntimeError as error:
        # Errors happen fairly often, DHT's are hard to read, just keep going
        print(error.args[0])
        time.sleep(2.0)
        continue
    except Exception as error:
        dhtDevice.exit()
        raise error

    time.sleep(2.0)
    if( temperature_c <= 25):
        ib.motor_1.throttle = 1.0
        ib.motor_2.throttle = -1.0
        ib.arcoiris = 50
    if( temperature_c > 25):
        ib.motor_1.throttle = 0
        ib.motor_2.throttle = 0
        ib.arcoiris = 10
    
