#!/usr/bin/python3

import socket
import subprocess
import time

cmd = 'python3'


def client_1():
    time.sleep(1)
    flag = subprocess.check_output([cmd, './client_1.py']).decode().strip()
    print("SCOREBOT client_1:")
    NAME = ["arianna.bianchi", "carlo.bettelini", "johan.jacob"]
    for n in NAME:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_address = ('10.40.0.46', 11111)
        s.connect(server_address)
        scorebot = n + " 1 " + flag
        s.send(scorebot.encode())
        response_flag = s.recv(1024)
        print(response_flag.decode())
        s.close()
        time.sleep(1)

def client_2():
    time.sleep(1)
    flag = subprocess.check_output([cmd, './client_2.py']).decode().strip()
    flag = flag.split()[1]
    print("SCOREBOT client_2:")
    NAME = ["arianna.bianchi", "carlo.bettelini", "johan.jacob"]
    for n in NAME:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_address = ('10.40.0.46', 11111)
        s.connect(server_address)
        scorebot = n + " 2 " + flag
        s.send(scorebot.encode())
        response_flag = s.recv(1024)
        print(response_flag.decode())
        s.close()
        time.sleep(1)

def client_4():
    time.sleep(1)
    flag = subprocess.check_output([cmd, './client_4.py']).decode().strip()
    flag = flag.split()[5]
    print("SCOREBOT client_4:")
    NAME = ["arianna.bianchi", "carlo.bettelini", "johan.jacob"]
    for n in NAME:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_address = ('10.40.0.46', 11111)
        s.connect(server_address)
        scorebot = n + " 4 " + flag
        s.send(scorebot.encode())
        response_flag = s.recv(1024)
        print(response_flag.decode())
        s.close()
        time.sleep(1)

def client_5():
    time.sleep(1)
    flag = subprocess.check_output([cmd, './client_5.py']).decode().strip()
    flag = flag.split()[7]
    print("SCOREBOT client_5:")
    NAME = ["arianna.bianchi", "carlo.bettelini", "johan.jacob"]
    for n in NAME:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_address = ('10.40.0.46', 11111)
        s.connect(server_address)
        scorebot = n + " 5 " + flag
        s.send(scorebot.encode())
        response_flag = s.recv(1024)
        print(response_flag.decode())
        s.close()
        time.sleep(1)

def client_8():
    time.sleep(1)
    flag = subprocess.check_output([cmd, './client_8.py']).decode().strip()
    flag = flag.split()[34]
    print("SCOREBOT client_8:")
    NAME = ["arianna.bianchi", "carlo.bettelini", "johan.jacob"]
    for n in NAME:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_address = ('10.40.0.46', 11111)
        s.connect(server_address)
        scorebot = n + " 8 " + flag
        s.send(scorebot.encode())
        response_flag = s.recv(1024)
        print(response_flag.decode())
        s.close()
        time.sleep(1)


client_1()
client_2()
client_4()
client_5()
client_8()
