import socket

DEST_IP = '10.40.0.46'
DEST_PORT = 9995


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    sock.connect((DEST_IP, DEST_PORT))
    sock.send("SYN Seq=0".encode())
    sock.recv(1024)
    sock.send("ACK Seq=1".encode())
    sock.close

if __name__ == "__main__":
    main()
