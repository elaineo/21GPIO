## GPIO test for Raspberry Pi

# import pin controller
from periphery import GPIO

import time

# Open GPIO 6 with output direction
gpio_out = GPIO(6, "out")

gpio_out.write(True)

# sleep for 5 seconds
time.sleep(5)

gpio_out.write(False)

gpio_out.close()