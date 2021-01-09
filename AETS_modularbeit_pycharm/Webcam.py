import time
import os

def take_picture():
    os.system('fswebcam -v -i 0 -d v4l2:/dev/video0 -r 1920x1080 -S 5 --jpeg 100 --save image.jpg')
    #now lets do this on an event ( authorized mail is there)
