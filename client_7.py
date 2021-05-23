import random
import socket
import random


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
sock.connect(('10.40.0.46', 9996))
Seq = random.randint(1, 10)
Ack = Seq + 4
FIN = "FIN,ACK Seq=" + str(Seq) + " Ack=" + str(Ack)
sock.send(FIN.encode())
print(FIN)
res1 = sock.recv(1024)
print(res1.decode())
Ack2 = Ack + 1
Seq2 = Seq + 1
ACK = "ACK Seq=" + str(int(Seq2)) + " Ack=" + str(Ack2)
sock.send(ACK.encode())
print(ACK)
res2 = sock.recv(1024)
print(res2.decode())
sock.close
