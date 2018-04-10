#https://www.raspberrypi.org/documentation/usage/camera/python/
import picamera
from time import sleep

#Create instance of PiCamera
camera = picamera.PiCamera()

#Video recording for 5 seconds
camera.start_recording('video1.h264')
sleep(5)
camera.stop_recording()

print("Recording done")
