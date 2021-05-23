#!/usr/bin/python3

import socket

DEST_IP = '10.40.0.46'
DEST_PORT = 9992


def main():
    sock1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    sock2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)

    sock1.connect((DEST_IP, DEST_PORT))
    data = sock1.recv(128)
    sock1.close()

    new_port = int(data.decode('ascii').replace('random port: ', ''))

    sock2.connect((DEST_IP, new_port))
    data = sock2.recv(128)
    print(data.decode('utf-8'))
    sock2.close()


if __name__ == "__main__":
    main()
