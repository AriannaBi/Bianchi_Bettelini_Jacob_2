#!/usr/bin/python3

import socket
import time


client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
client_socket.connect(('10.40.0.46', 9991))
message = "helo"
client_socket.send(message.encode())
modified_message, server_address = client_socket.recvfrom(2048)
print(message)
print(modified_message.decode())

client_socket.close()