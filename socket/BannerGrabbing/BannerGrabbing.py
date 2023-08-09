#!/usr/bin/python
#Banner grabbing é uma técnica usada em segurança cibernética para coletar informações sobre um sistema remoto, 
#como servidores web, servidores de email e outros dispositivos conectados em rede.

import socket

#Solicitar input
print("Banner grabbing by El3tr0n1c")
ip = str(input("Digite o endereço IP do alvo: "))
porta = int(input("Digite a porta: "))

#realizar conexão
meusocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conecta = meusocket.connect_ex((ip,porta))
#exibir banner
banner = meusocket.recv(1024)
print(banner.decode)

user = input("Digite um usuário: ")
senha = input("Digite a senha: ")

meusocket.send("USER %s\r\n" %user.encode())
banner = meusocket.recv(1024)
print (banner.decode())

#Enviar credenciais e exibir banner resposta
meusocket.send("PASS %s\r\n" %senha.encode())
banner = meusocket.recv(1024)
print (banner.decode())

meusocket.close()
