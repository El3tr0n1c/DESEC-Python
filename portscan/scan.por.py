#!/usr/bin/python
import socket

ip = input("Digite o endereço IP do alvo: ")

for porta in range(1,65535):
    
    meusocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    if meusocket.connect_ex((ip,porta)) == 0:
        print ("PORTA %i [ABERTA]: " %porta)
        meusocket.close()