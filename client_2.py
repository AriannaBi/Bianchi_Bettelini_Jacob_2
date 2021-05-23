#!/usr/bin/python3

import socket
import time

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

    # # Scorebot
    # print("SCOREBOT:")
    # NAME = ["arianna.bianchi", "carlo.bettelini", "johan.jacob"]
    # for n in NAME:
    #     s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #     server_address = ('10.40.0.46', 11111)
    #     s.connect(server_address)
    #     scorebot = n + " 2 " + modified_message.decode()
    #     s.send(scorebot.encode())
    #     response_flag = s.recv(1024)
    #     print(response_flag.decode())
    #     s.close()
    #     time.sleep(1)


if __name__ == "__main__":
    main()
