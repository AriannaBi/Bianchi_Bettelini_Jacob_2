#!/usr/bin/python3

import socket
import subprocess
import time
import base64

cmd = 'python3'


def client_1():
    time.sleep(1)
    flag = subprocess.check_output([cmd, './client_1.py']).decode().strip()
    print(flag)
    print("SCOREBOT client_1:")
    NAME = ["arianna.bianchi", "carlo.bettelini", "johan.jacob"]
    for n in NAME:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_address = ('10.40.0.46', 11111)
        s.connect(server_address)
        scorebot = n + " 1 " + flag
        s.send(scorebot.encode())
        response_flag = s.recv(1024)
        print(n + " "+ response_flag.decode())
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
        print(n + " "+ response_flag.decode())
        s.close()
        time.sleep(1)

def client_3():
    time.sleep(1)
    flag = subprocess.check_output([cmd, './client_3.py']).decode().strip()
    flag = flag.split()[3]
    print("SCOREBOT client_3:")
    NAME = ["arianna.bianchi", "carlo.bettelini", "johan.jacob"]
    for n in NAME:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_address = ('10.40.0.46', 11111)
        s.connect(server_address)
        scorebot = n + " 3 " + flag
        s.send(scorebot.encode())
        response_flag = s.recv(1024)
        print(n + " "+ response_flag.decode())
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
        print(n + " "+ response_flag.decode())
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
        print(n + " "+ response_flag.decode())
        s.close()
        time.sleep(1)

def client_6():
    time.sleep(1)
    flag = subprocess.check_output([cmd, './client_6.py']).decode().strip()
    flag = flag.split()[8]
    print("SCOREBOT client_6:")
    NAME = ["arianna.bianchi", "carlo.bettelini", "johan.jacob"]
    for n in NAME:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_address = ('10.40.0.46', 11111)
        s.connect(server_address)
        scorebot = n + " 6 " + flag
        s.send(scorebot.encode())
        response_flag = s.recv(1024)
        print(n + " "+ response_flag.decode())
        s.close()
        time.sleep(1)

def client_7():
    time.sleep(1)
    flag = subprocess.check_output([cmd, './client_7.py']).decode().strip()
    flag = flag.split()[12]
    print("SCOREBOT client_7:")
    NAME = ["arianna.bianchi", "carlo.bettelini", "johan.jacob"]
    for n in NAME:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_address = ('10.40.0.46', 11111)
        s.connect(server_address)
        scorebot = n + " 7 " + flag
        s.send(scorebot.encode())
        response_flag = s.recv(1024)
        print(n + " "+ response_flag.decode())
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
        print(n + " "+ response_flag.decode())
        s.close()
        time.sleep(1)

def client_9():
    time.sleep(1)
    flag = subprocess.check_output([cmd, './client_9.py']).decode().strip()
    flag = flag.split()[24]
    flag = base64.b64decode(flag).decode()
    print("SCOREBOT client_9:")
    NAME = ["arianna.bianchi", "carlo.bettelini", "johan.jacob"]
    for n in NAME:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_address = ('10.40.0.46', 11111)
        s.connect(server_address)
        scorebot = n + " 9 " + flag
        s.send(scorebot.encode())
        response_flag = s.recv(1024)
        print(n + " "+ response_flag.decode())
        s.close()
        time.sleep(1)


def client_10():
    time.sleep(1)
    flag = subprocess.check_output([cmd, './client_10.py']).decode().strip()
    flag = flag.split()[3]
    print("SCOREBOT client_10:")
    NAME = ["arianna.bianchi", "carlo.bettelini", "johan.jacob"]
    for n in NAME:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_address = ('10.40.0.46', 11111)
        s.connect(server_address)
        scorebot = n + " 10 " + flag
        s.send(scorebot.encode())
        response_flag = s.recv(1024)
        print(n + " "+ response_flag.decode())
        s.close()
        time.sleep(1)


client_1()
client_2()
client_3()
client_4()
client_5()
client_6()
client_7()
client_8()
client_9()
client_10()
