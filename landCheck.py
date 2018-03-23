#http://www.catb.org/gpsd/gpsd_json.html(Choose TPV object for keys)

from gps3 import gps3
import subprocess
import sys
from time import sleep

#flightMode is the current stage of flight
#l = launchpad
#a = ascent
#d = descent
#c = crash/landing (most likely crash)
flightMode = 'l'

#altitude = 0
#climb is the vertical velocity (positive value for up, negative value for down)
climb = 0
#climbOffset is the climb error value
#climbOffset = 0.18
#maxClimb is the largest climb value found
maxClimb = 0

#Command line commands to set up gps
subprocess.call(["sudo", "systemctl", "stop", "gpsd.socket"])
subprocess.call(["sudo", "systemctl", "disable", "gpsd.socket"])
subprocess.call(["sudo", "systemctl", "stop", "gpsd.socket"])
subprocess.call(["sudo", "killall","gpsd"])
subprocess.call(["sudo", "gpsd", "/dev/ttyS0", "-F", "/var/run/gpsd.sock"])

#GPS variables
gps_socket = gps3.GPSDSocket()
data_stream = gps3.DataStream()

#Establish connection to serial port
gps_socket.connect()
gps_socket.watch()

try:
	#Check for new data
	for new_data in gps_socket:
		if new_data:
			#Unpack data for data access
			data_stream.unpack(new_data)
			#Assign altitude and climb new values
			#altitude = data_stream.TPV['alt']
			#Wait until GPS has lock
#			print('Climb error = ',data_stream.TPV['epc']
			if ((data_stream.TPV['climb'] == 'n/a')):
				print("GPS does not have lock")
				continue
#
			climb = float(data_stream.TPV['climb'])
			print ("Climb = ", climb)
			if (abs(maxClimb) < abs(climb)):
				maxClimb = climb
#			climbOffset = int(data_stream.TPV['epc'])
#			#If the rocket is moving upward from the launchpad (climb is positive), flightMode is in ascent
#			if (climb - climbOffset > 0 and flightMode == 'l'):
#				flightMode = 'a'
#			#If the rocket is moving downward while in ascent mode (climb is negative), flightMode is in descent
#			elif (climb < 0 and flightMode == 'a'):
#				flightMode = 'd'
#			#If the rocket has stopped moving while in descent mode, flightMode is in crash
#			elif ((climb - climbOffset == 0 or climb + climbOffset == 0) and flightMode == 'd'):
#				flightMode = 'c'
#			#Print statements for testing
#			print(climb)
#			print(climbOffset)
#			print(flightMode)
#			time.sleep(.1)

except StopIteration:
	print ("Max Climb = ", maxClimb)
	data_stream = None
	gps_socket = None
	print ("GPSD has terminated")

except KeyboardInterrupt:
	print ("Max Climb = ", maxClimb)
	print("We killed it")
	sys.exit()
