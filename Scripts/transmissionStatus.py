import RPi.GPIO as GPIO
import transmissionrpc
import getpass
from time import sleep
#End imports



#LED Mapping
red = 22
green = 23
blue = 24
#=== GPIO Setup ===#
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
#GPIO.setup(23, GPIO.OUT)
#GPIO.setup(24, GPIO.OUT)
#======End GPIO Setup======#
rpcUrl = raw_input("Transmission URL: ")
rpcPort = raw_input("Port: ")
rpcUser = raw_input("Username: ")
rpcPass = getpass.getpass("Password: ")
#=============================#
tc = transmissionrpc.Client(address=rpcUrl, port=rpcPort, user=rpcUser, password=rpcPass)
torrent = tc.get_torrent(1)
status = torrent.status
print status
sleep(3)



'''
    GPIO.setmode(GPIO.BMC)
    GPIO.setup(22, GPIO.OUT)
'''
#============================#
if status == "stopped":
	GPIO.setup(22, GPIO.OUT)
    GPIO.output(22, 1)
    print "Stopped"
elif status == "download pending":
   print "Queued"
elif status == "paused":
   print "Paused"
else:
   print "Failure"

#=======================
print "Done"
sleep(5)
GPIO.cleanup()
