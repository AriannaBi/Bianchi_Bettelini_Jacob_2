#!/usr/bin/python3

import socket
from decimal import Decimal
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('10.40.0.46', 9997)
s.connect(server_address)

get = "GET / HTTP/1.0\r\n" + "Host: 10.40.0.46:9997\r\n\n"

s.send(get.encode())
request = s.recv(1024)
request = request.decode()
print(get)
print(request)
requestq = s.recv(1024)
requestq = requestq.decode()
print(requestq)

s.close()


# # Scorebot
# if not requestq:
#     flag = request.split()[29]
# else:
#     flag = requestq.split()[5]
#
# print("SCOREBOT:")
# NAME = ["arianna.bianchi", "carlo.bettelini", "johan.jacob"]
# for n in NAME:
#     s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     server_address = ('10.40.0.46', 11111)
#     s.connect(server_address)
#     scorebot = n + " 8 " + flag
#     s.send(scorebot.encode())
#     response_flag = s.recv(1024)
#     print(response_flag.decode())
#     s.close()
#     time.sleep(1)