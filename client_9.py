#!/usr/bin/python3

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('10.40.0.46', 9998)
s.connect(server_address)

post = "POST / HTTP/1.0\r\n" + "Host: 10.40.0.46:9998\r\n" + "Content-Type: application/text\r\n" \
       + "Content-Length: 0\r\n\n"

s.send(post.encode())
request = s.recv(1024)
request = request.decode()
print(post)
print(request)
requestq = s.recv(1024)
requestq = requestq.decode()
print(requestq)

s.close()