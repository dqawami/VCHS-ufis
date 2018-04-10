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

#Check for new data
for new_data in gps_socket:
	if new_data:
		#Unpack data for data access
		data_stream.unpack(new_data)
		print('Climb = ', data_stream.TPV['climb']) #http://www.catb.org/gpsd/gpsd_json.html(Choose TPV object for keys)

