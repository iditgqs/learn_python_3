# -*- coding:utf-8 -*-

from socket import *

import time

client_list = []

for i in range(11):
    client = socket(AF_INET, SOCK_STREAM)
    client.connect(("127.0.0.1", 8080))
    client_list.append(client)
    msg = "GET / HTTP/1.1"
    client.send(msg.encode("utf-8"))
    print(client.recv(1024))

for client in client_list:
    time.sleep(0.5)
    client.close()
