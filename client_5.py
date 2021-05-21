#!/usr/bin/python3

import socket
from decimal import Decimal


def convert_measure(n):
    if n == 'Kb':
        return 1000
    elif n == 'Mb':
        return 1000000
    elif n == 'Gb':
        return 1000000000
    elif n == 'bits':
        return 1


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('10.40.0.46', 9994)
s.connect(server_address)

request = s.recv(1024)
request = request.decode()
print(request)

#Create the array
L = request.split()
# print(L)

#Retrieve the number
numberL = L[0].split('=')[1]
numberR1 = L[2].split('=')[1]
numberR2 = L[4].split('=')[1]

#Convert the number in bits
numberL = Decimal(numberL) * convert_measure(L[1])
numberR1 = Decimal(numberR1) * convert_measure(L[3][:2])
numberR2 = Decimal(numberR2) * convert_measure(L[5][:2])

#Formula for store and forward
result = str((numberL/numberR1) + (numberL/numberR2))
print(result)

#Send the result and receive the flag
s.send(result.encode())
request = s.recv(1024)
request = request.decode()
print(request)

s.close()