#!/usr/bin/env python
import socket
import subprocess
import sys
from datetime import datetime

# Scan all ports open on host
def doTheAllThing():
	t1 = datetime.now()
	try:
	    for port in xrange(0,65536):  
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		result = sock.connect_ex((remoteServerIP, port))
		if result == 0:
		    print "Port {}: 	 Open".format(port)
		sock.close()
	    	
	    # Checking the time again
	    t2 = datetime.now()

	    # Calculates the difference of time, to see how long it took to run the script
	    total =  t2 - t1

	    # Printing the information to screen
	    print 'Scanning Completed in: ', total
	    sys.exit()

	except KeyboardInterrupt:
	    sys.exit()

	except socket.gaierror:
	    print 'Hostname could not be resolved. Exiting'
	    sys.exit()

	except socket.error:
	    print "Couldn't connect to server"
	    sys.exit()



# Use for single port scan
def singlePort():
	try:
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		resultS = sock.connect_ex((remoteServerIP, int(remotePort)))
		if resultS == 0:
			print "Port {}: 	 Open".format(remotePort)
		else:
			print "Port {}: 	 Closed".format(remotePort)
		sock.close()

	except KeyboardInterrupt:
	    #print "You pressed Ctrl+C"
	    sys.exit()

	except socket.gaierror:
	    print 'Hostname could not be resolved. Exiting'
	    sys.exit()

	except socket.error:
	    print "Couldn't connect to server"
	    sys.exit()

# Obtain what ports need to be scanned
def getPort(prompt="Enter port number or 'all' to scan ports (type done when finished): "):
	#while True:
		try:
			x = raw_input(prompt)
			if x.lower() == 'all':
				doTheAllThing()
			if x.lower() == '':
				return x
			return int(x)
		except ValueError:
			print 'Invalid input'
			x = ''

def server():
	while True:
		remoteServer = raw_input("Enter another host to scan or press Enter to finish: ")
		if remoteServer != '':
			server.append(remoteServer)
		else:
			break

def portsIteration():
	ports = 'x'
	while ports != '':
		ports = getPort()
		if ports != '':
			array.append(ports)

		#removes any invalid inputs from array
		if array.count(None) > 0:
			array.remove(None)

# Clear the screen
#subprocess.call('clear', shell=True)

# Get IP addresses
remoteServer = raw_input("Enter a remote host to scan: ")
remoteServerIP = socket.gethostbyname(remoteServer)
server = []
server.append(remoteServer)

# Entering multiple server IP addresses
#server()

# Getting all Ports
socket.setdefaulttimeout(.0006)
array = []
portsIteration()

# Print a nice banner with information on which host we are about to scan
print "-" * 60
print "Please wait, scanning remote host", remoteServerIP
print "-" * 60

# Using the range function to specify ports (scans all ports listed by user)
if array > 1:
	for port in range(len(array)): 
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		result = sock.connect_ex((remoteServerIP, int(array[port])))
		if result == 0:
		    	print "Port {}: 	 Open".format(int(array[port]))
		if result == 111:
			print "Port {}: 	 Closed".format(int(array[port]))
		sock.close()

