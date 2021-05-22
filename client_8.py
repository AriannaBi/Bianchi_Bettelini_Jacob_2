#!/usr/bin/python3

import socket
from decimal import Decimal
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('10.40.0.46', 9997)
s.connect(server_address)

get = "GET / HTTP/1.0\r\n" + "Host:10.40.0.46:9997\r\n\n"

s.send(get.encode())
request = s.recv(1024)
request = request.decode()
print(get)
print(request)

s.close()


#Scorebot
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('10.40.0.46', 11111)
s.connect(server_address)

request = request.split()[34]
print(request)
NAME = ["arianna.bianchi", "carlo.bettelini", "johan.jacob"]
for n in NAME:
    scorebot = n + " 8 " + request
    s.send(scorebot.encode())
    response_flag = s.recv(1024)
    print(response_flag.decode())
    time.sleep(1)

s.close()