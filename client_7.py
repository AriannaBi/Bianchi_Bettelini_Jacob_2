import random
import socket
import random

DEST_IP = '10.40.0.46'
DEST_PORT = 9996


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    sock.connect((DEST_IP, DEST_PORT))
    Seq = random.randint(0, 10)
    Ack = random.randint(0, 10)
    FIN = "FIN,ACK Seq=" + str(Seq) + " Ack=" + str(Ack)
    sock.send(FIN.encode())
    print(FIN)
    res1 = sock.recv(1024)
    print(res1.decode())
    Ack2 = random.randint(0, 10)
    ACK = "ACK, Seq=" + str(Ack) + " Ack=" + str(Ack2)
    sock.send(ACK.encode())
    print(ACK)
    res2 = sock.recv(1024)
    print(res2.decode())
    sock.close


if __name__ == "__main__":
    main()
