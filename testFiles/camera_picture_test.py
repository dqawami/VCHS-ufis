#https://www.raspberrypi.org/documentation/usage/camera/python/
import picamera
from time import sleep

#Create instance of PiCamera
camera = picamera.PiCamera()

#Take two pictures with a 5 second delay
camera.capture('image1.jpg')
sleep(5)
camera.capture('image2.jpg')

print("Pictures taken")

