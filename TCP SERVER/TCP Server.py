#!/usr/bin/python3

import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 777

server.bind(("192.168.1.150", port))
server.listen(3)

while (True):

    clientSocket, address = server.accept();

    print("Received connection from: %s" % str(address))

    message = "Hello Hacker, Welcome to server" + "\r\n"

    clientSocket.send(message.encode("ascii"));

    clientSocket.close()
