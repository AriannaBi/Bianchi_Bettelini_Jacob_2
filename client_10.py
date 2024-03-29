# Python program to sum of two numbers
# using bitwise operator

import socket
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('10.40.0.46', 9999)
s.connect(server_address)

request = s.recv(1024).decode()
print(request)

number1 = request.split()[0]
number2 = request.split()[1]

A = [int(x) for x in str(number1)]
B = [int(a) for a in str(number2)]

checksum = ''
carry = 0
while True:
    if len(str(checksum)) != 8:
        if checksum != '':
            carry = int(str(checksum)[0])
            checksum = checksum[1:]
            A = [int(x) for x in str(checksum)]
            checksum = ''
            B = [0,0,0,0,0,0,0,0]
        for i in range(7,-1,-1):
            if A[i] == 0 and B[i] == 0:
                if carry == 1:
                    checksum += '1'
                    carry = 0
                else:
                    checksum += '0'
                    carry = 0
            elif (A[i] == 1 and B[i] == 0) or (A[i] == 0 and B[i] == 1):
                if carry == 1:
                    checksum += '0'
                    carry = 1
                else:
                    checksum += '1'
                    carry = 0
            elif A[i] == 1 and B[i] == 1:
                if carry == 1:
                    checksum += '1'
                    carry = 1
                else:
                    checksum += '0'
                    carry = 1
        if carry == 1:
            checksum += str(carry)
            checksum = checksum[::-1]
        else:
            checksum = checksum[::-1]
    else:
        break

array = str(checksum)
flipbits = ''

for bit in array:
    if bit == '0':
        flipbits += '1'
    else:
        flipbits += '0'

print(flipbits)
s.send(flipbits.encode())

flag = s.recv(1024)
print(flag.decode())

s.close()
