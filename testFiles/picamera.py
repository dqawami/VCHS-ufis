import picamera #https://www.raspberrypi.org/documentation/usage/camera/python/
from time import sleep

#Instance of picamera class
camera = picamera.PiCamera()

#Take a picture
camera.capture('image1.jpg')
sleep(5)
#Take a second picture five seconds later
camera.capture('image2.jpg)

#Video recording for five seconds
camera.start_recording('video.h264')
sleep(5)
camera.stop_recording()
