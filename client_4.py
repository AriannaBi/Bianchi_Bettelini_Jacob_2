from socket import *

serverName = "10.40.0.46:9993"
serverPort = 80

clientSocket = socket(AF_INET, SOCK_STREAM)

clientSocket.connect((serverName,serverPort))

x, y = input('')

clientSocket.close()

ratio = x/y

clientSocket.send(ratio.encode())
