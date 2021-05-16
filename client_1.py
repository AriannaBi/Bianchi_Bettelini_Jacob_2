#!/usr/bin/python3

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('10.40.0.46', 9990)
s.connect(server_address)

request = s.recv(1024)
print(request.decode())
s.close()