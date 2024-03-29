#!/usr/bin/python3

import socket

# Hash map for unit conversion. Values are converted into either Kbits or Kibits.
# Why not converting all in bits?
hash_map = {
    'Kbit': 1,
    'Mbit': 1000,
    'Gbit': 1000*1000,
    'Kibit': 1,
    'Mibit': 1024,
    'Gibit': 1024*1024
}

sep = '\n'  # Used to add a separator to the string for sending the resulting ratio to the server
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('10.40.0.46', 9993))
to_compute = client_socket.recv(1024)
print(to_compute.decode())

# Divide the message received from the server into an array.
infos = to_compute.decode().split()

x, y = int(infos[0]), int(infos[2])

# Convert values if they are not in Kibit/Kbit
x *= hash_map[infos[1]]
y *= hash_map[infos[3]]

# Make x and y of the same unit value
if len(infos[3]) == 4:
    y /= 1.024
else:
    x /= 1.024

ratio = x / y
print(ratio)

val = str(ratio) + sep
client_socket.send(val.encode())
flag = client_socket.recv(2048)
print(flag.decode())
client_socket.close()
