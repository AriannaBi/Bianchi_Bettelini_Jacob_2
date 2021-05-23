import socket


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
sock.connect(('10.40.0.46', 9995))
sock.send("SYN Seq=0".encode())
print("SYN Seq=0")
res1 = sock.recv(1024)
print(res1.decode())
sock.send("ACK Seq=1 Ack=1".encode())
print("ACK Seq=1 Ack=1")
res2 = sock.recv(1024)
print(res2.decode())
sock.close
