#import RPi.GPIO as GPIO
import transmissionrpc
import getpass
#End imports



#LED Mapping
red = 22
green = 23
blue = 24
#=== GPIO Setup ===#
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(red, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)
GPIO.setup(blue, GPIO.OUT)
#Color Sets
setRed = GPIO.output(red, 1)
setBlue = GPIO.output(green, 1)
setGreen = GPIO.output(blue, 1)
setYellow = GPIO.cleanup()
#======End GPIO Setup======#
rpcUrl = raw_input("Transmission URL: ")
rpcPort = raw_input("Port: ")
rpcUser = raw_input("Username: ")
rpcPass = getpass.getpass("Password: ")
#=============================#
tc = transmissionrpc.Client(address=rpcUrl, port=rpcPort, user=rpcUser, password=rpcPass)
torrent = tc.get_torrent(1)
status = torrent.status
#============================#
if status == "stopped":
   setRed
elif status == "download pending":
   setBlue
elif status == "paused":
   setYellow
else:
   setGreen
   GPIO.cleanup()
