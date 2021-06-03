#!/usr/bin/python3

import socket
sock1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
sock2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
sock1.connect(('10.40.0.46', 9992))
data = sock1.recv(128)
sock1.close()
new_port = int(data.decode('ascii').replace('random port: ', '')) # why decoding with "ascii" instead of "utf-8" ?
print("random port: " + str(new_port))
sock2.connect(('10.40.0.46', new_port))
data = sock2.recv(128)
print(data.decode('utf-8'))
sock2.close()

