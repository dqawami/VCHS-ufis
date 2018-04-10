from gps3 import gps3
import subprocess

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

#Check for new data and save in file
try:
	for new_data in gps_socket:
		if new_data:
			#Unpack data for data access
			data_stream.unpack(new_data)
			
			#Print out climb(vertical velocity value)
			print('Climb = ', data_stream.TPV['climb'])

#Code interrupts upon keyboard interrupt(Contorl + C)
except KeyboardInterrupt:
	print("GPS code has been killed") 
	
	#Destroying gps instances 
	gps_socket = None
	data_stream = None
	
	#Code quits 
	quit()
