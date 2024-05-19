#!/usr/bin/python3

import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname();
port = 777

client.connect("192.168.1.1", port)

message = client.recv(1024)

client.close()

print(message.decode("ascii"))
