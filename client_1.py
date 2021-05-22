#!/usr/bin/python3

import socket
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('10.40.0.46', 9990)
s.connect(server_address)

request = s.recv(1024).decode()
print(request)
s.close()


#Scorebot
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('10.40.0.46', 11111)
s.connect(server_address)

NAME = ["arianna.bianchi", "carlo.bettelini", "johan.jacob"]
for n in NAME:
    scorebot = n + " 1 " + request
    s.send(scorebot.encode())
    response_flag = s.recv(1024)
    print(response_flag.decode())
    time.sleep(1)

s.close()