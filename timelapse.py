
import mss
import time

# variables
monitor = 1
record = True
shotNumber = 1
intervalSec = 5

# functions


def takeScreenshot(mon=1):
    with mss.mss() as mss_instance:
        mss_instance.shot(mon=monitor, output=str(shotNumber)+".png")


# app
while record == True:
    takeScreenshot()
    time.sleep(intervalSec)
    shotNumber += 1
