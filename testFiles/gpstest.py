from gps3 import gps3
import subprocess

subprocess.call(["sudo", "systemctl", "stop", "gpsd.socket"])
subprocess.call(["sudo", "systemctl", "disable", "gpsd.socket"])
subprocess.call(["sudo", "systemctl", "stop", "gpsd.socket"])
subprocess.call(["sudo", "killall","gpsd"])
subprocess.call(["sudo", "gpsd", "/dev/ttyS0", "-F", "/var/run/gpsd.sock"])

gps_socket = gps3.GPSDSocket()
data_stream = gps3.DataStream()
gps_socket.connect()
gps_socket.watch()
for new_data in gps_socket:
	if new_data:
		data_stream.unpack(new_data)
		print('Altitude = ', data_stream.TPV['alt'])

