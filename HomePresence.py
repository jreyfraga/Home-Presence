# Simple Python script that list LAN connected users

import os
import time
import sys
import signal

cacheFileName = "ARPScanCache"
cacheFile = str(cacheFileName)
systemCommand = "sudo arp-scan -l > " + cacheFile

# List here the MAC and name of the users you want to check in your LAN
devices ={'Jhon': "00:00:00:00:00:00",
'Paul': "00:00:00:00:00:00",
'Mary': "00:00:00:00:00:00"}

def checkConnectedUsers():
	usersConnected = 0
	os.system(systemCommand)
	with open(cacheFile) as CacheBuffer:
		for user in devices:
			CacheBuffer.seek(0)
			for line in CacheBuffer.readlines():
				if devices[user] in line:
					usersConnected = usersConnected + 1
					print user, "is connected."
	return usersConnected

def signal_handler(signal, frame):
	print "Control + C exit"
	sys.exit(0)

if __name__ == "__main__":
	signal.signal(signal.SIGINT, signal_handler)
	if checkConnectedUsers() is 0:
		print "Not users connected."
