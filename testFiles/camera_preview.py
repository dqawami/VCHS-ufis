#https://www.raspberrypi.org/documentation/usage/camera/python/
import picamera
from time import sleep

#Create instance of PiCamera
camera = picamera.PiCamera()

#Start Camera preview(Control-D terminates the preview(Remember this!!!))
camera.start_preview()
