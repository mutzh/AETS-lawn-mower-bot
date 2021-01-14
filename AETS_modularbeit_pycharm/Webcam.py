#takes a picture with linux module "fswebcam" and saves it as "filename", where filename has to be a string

def take_picture(filename):
    import os
    os.system('fswebcam -v -i 0 -d v4l2:/dev/video0 -r 1920x1080 -S 5 --jpeg 100 --save' +' '+filename)

