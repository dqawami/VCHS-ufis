from gps3 import gps3 #Link: https://pypi.python.org/pypi/gps3/
import subprocess
import pygame #Link: http://www.stuffaboutcode.com/2016/05/raspberry-pi-playing-sound-file-with.html
import time

#GPS variables
gps_socket = 0 #Socket connection for serial port to GPS
data_stream = 0 #Contains all gps data 
gps_alt = 0 #GPS altitude

#TBD
song_path_1 = 0
song_path_2 = 0

#Initialise pygame and the mixer
pygame.init()
pygame.mixer.init()


def gps_init(): #http://www.catb.org/gpsd/gpsd_json.html (look for TPV object)
    #Terminal commands to set up GPS
    subprocess.call(["sudo", "systemctl", "stop", "serial-getty@ttyAMA0.service"])
    subprocess.call(["sudo", "systemctl", "disable", "serial-getty@ttyAMA0.service"])
    subprocess.call(["sudo", "killall", "gpsd"])
    subprocess.call(["sudo", "gpsd", "/dev/ttyAMA0", "-F", "/var/run/gpsd.sock"])

    global gps_socket
    global data_stream
    
    gps_socket = gps3.GPSDSocket()
    data_stream = gps3.DataStream()
    
    #Connect to serial port
    gps_socket.connect()
    
    #Begin data collection
    data_stream.watch()

#main method
for new_data in gps_socket:
    if new_data: #Checks if there is new data
        #Makes data accessible 
        data_stream.unpack(new_data)
        print('Altitude = ', data_stream.TPV['alt']) #look at link above at gps_init for tpv key terms

        while(data_stream.TPV['alt'] > gps_alt):
            gps_alt = data_stream.TPV['alt']

        pygame.mixer.music.load("myFile.wav") #Find file path
        pygame.mixer.music.play()

        
