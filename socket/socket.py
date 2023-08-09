#!/usr/bin/python

import socket
ip = str(input("Digite o endereço IP: "))
porta = int(input("Digite a porta: "))
#SOCK_STREAM = TCP
meusocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#connect_ex retorna 0 se obteve exito
resposta = meusocket.connect_ex((ip,porta))

if (resposta == 0):
    print("Porta: %d ABERTA. " %porta)
    
else:
    (print("Porta %d FECHADA. " %porta))
    
    