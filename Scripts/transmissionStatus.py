#import RPi.GPIO as GPIO
import transmissionrpc
import getpass
#End imports
'''
#=== GPIO Setup ===#
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
#======End GPIO Setup======#
'''

#rpcUrl = raw_input("Transmission URL: ")
rpcUrl = "192.168.0.45"
rpcPort = raw_input("Port: ")
rpcUser = raw_input("Username: ")
rpcPass = getpass.getpass("Password: ")
#=============================#
'''
#tc = transmissionrpc.Client(address=rpcUrl, port=rpcPort, user=rpcUser, password=rpcPass)

tc = transmissionrpc.Client('192.168.0.45', port=9091, user='has', password='asdf123')
torrent = tc.get_torrent(2)
status = torrent.status

#============================#
if status == "stopped":
   print torrent.name,"  :Torrent stopped!"
elif status == "download pending":
   print "Download Queued"
elif status == "paused":
   print "Download Paused"
else:
   print "Torrent doing something else?"
