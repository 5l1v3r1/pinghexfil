#!/usr/bin/python
# get file length (bytes) / 30000
# and determine the amount of ICMP packets required
# 30,000 is 60,000/2 as the data is "hexlified" for stealth
#
#
import os
import sys
def usage():
    print """
 PingHexFil - File-Analysis
 2019 WeakNetLabs
 Usage: ./file-analysis.py (FILE)
"""
# I think this needs built right into the main app.
