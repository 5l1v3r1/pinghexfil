#!/usr/bin/python
# This will decode the bytes from Wireshark into file output.
# 2019 - WeakNet Labs
import binascii
from sys import argv,exit
usage="Usage: ./decoder.py (FILE)"
fileData=""
if (len(argv)==2):
    print "[+] Opening file: "+argv[1]
    with open(argv[1],'rb') as byte:
        fileData+=byte.read()
else:
    print usage
    exit(1)
# done, print:
print "[+] file data: "+fileData
print fileData.strip().decode("hex")
