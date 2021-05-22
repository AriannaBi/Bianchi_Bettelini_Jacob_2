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


NAME = ["arianna.bianchi", "carlo.bettelini", "johan.jacob"]
for n in NAME:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('10.40.0.46', 11111)
    s.connect(server_address)
    scorebot = n + " 1 " + request
    s.send(scorebot.encode())
    response_flag = s.recv(1024)
    print(response_flag.decode())
    s.close()
    time.sleep(1)