#!/usr/bin/python3

import socket

DEST_IP = '10.40.0.46'
DEST_PORT = 9991


def main():

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)

    client_socket.connect((DEST_IP, DEST_PORT))

    message = "helo"
    client_socket.sendto(message.encode(), (DEST_IP, DEST_PORT))

    modified_message, server_address = client_socket.recvfrom(2048)

    print(message)
    print(modified_message.decode())

    client_socket.close()


if __name__ == "__main__":
    main()
