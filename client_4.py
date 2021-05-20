#!/usr/bin/python3

import socket

DEST_IP = '10.40.0.46'
DEST_PORT = 9993


def main():

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)

    client_socket.connect((DEST_IP, DEST_PORT))

    to_compute, server_address = client_socket.recv(1024)

    print(to_compute.decode())

    # Divide the message received from the server into an array.
    infos = to_compute.split()

    x, y = infos[0], infos[2]

    # Convert values if they are not in Kibit/Kbit
    if infos[1] == "Mibit":
        x *= 1024
    elif infos[1] == "Gibit":
        x *= 1024*1024

    if infos[3] == "Mbit":
        y *= 1000

    elif infos[3] == "Gbit":
        y *= 1000*1000

    ratio = x / y
    print(ratio)

    client_socket.sendto(ratio.encode(), (DEST_IP, DEST_PORT))

    flag, server_address = client_socket.recv(2048)

    print(flag.decode())

    client_socket.close()


if __name__ == "__main__":
    main()
