from gps3 import gps3
import subprocess

#Command line commands to set up gps
subprocess.call(["sudo", "systemctl", "stop", "gpsd.socket"])
subprocess.call(["sudo", "systemctl", "disable", "gpsd.socket"])
subprocess.call(["sudo", "systemctl", "stop", "gpsd.socket"])
subprocess.call(["sudo", "killall","gpsd"])
subprocess.call(["sudo", "gpsd", "/dev/ttyS0", "-F", "/var/run/gpsd.sock"])

#Initialize GPS variables
gps_socket = gps3.GPSDSocket()
data_stream = gps3.DataStream()

#Begin GPS connection to serial port for data stream
gps_socket.connect()
gps_socket.watch()

#Begin receiving new data from the gps
try:
        for new_data in gps_socket:
                if new_data:
                        #Unpack GPS data to access it
                        data_stream.unpack(new_data)

                        #Climb or vertical velocity value is accessed from TPV class
                        print('Climb ', data_stream.TPV['climb'])

#Code interrupt via Control-C
except KeyboardInterrupt:
        print("GPS has been killed")
        quit()
