# imports
import mss
import time
import os

# set variables here
folderRoot = "E:/screenshots"  # set your folder (must exists)
# folderRoot = "."  # to have it in the same folder as script
pauseSec = 5
monitor = 1
record = True
shotNumber = 1
verbose = False

# functions


def createNowFolder(folderRoot):
    """create a folder with nowd date-time as folder name"""
    folderName = time.strftime("%Y-%m-%e-%H-%M-%S")
    if os.path.isdir(folderName):
        if verbose:
            print("Folder already exists : " + folderName)
    else:
        print("Creating folder : " + folderName)
        os.makedirs(folderRoot+"/"+folderName)
    return folderName


def takeScreenshot(shotNumber, folderName, monitor=monitor):
    """takes screenshot with given number and optional monitor number"""
    with mss.mss() as mss_instance:
        mss_instance.shot(mon=monitor, output=folderRoot + "/" + folderName +
                          "/"+str(shotNumber)+".png")


# app
folderName = createNowFolder(folderRoot)
while record == True:
    takeScreenshot(shotNumber, folderName)
    time.sleep(pauseSec)
    shotNumber += 1
