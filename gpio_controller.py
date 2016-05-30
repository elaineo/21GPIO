import sys

# import pin controller
from periphery import GPIO

import time


def pull_up(pin, seconds):
    # Open GPIO 6 with output direction
    gpio_out = GPIO(pin, "out")

    # dispense some beans
    gpio_out.write(True)

    # This needs to be calibrated depending 
    # on dispenser speed. 
    time.sleep(seconds)

    # Stop spitting out beans
    gpio_out.write(False)
    gpio_out.close()


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Please enter a valid pin and duration')
    else:
        pull_up(int(sys.argv[1]), int(sys.argv[2]))