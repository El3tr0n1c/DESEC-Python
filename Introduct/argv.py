#!/usr/bin/python
import sys #trabalha com argumentos
import os #comandos do sistema operacional

#Dessa forma, você pode chamar o script já passando os argumentos (necessário importar sys)
#Exemplo: ./argv.py 192.168.0.1 80
print("Varrendo o host: ",sys.argv[1], "Na porta: ",sys.argv[2])

#Exemplo de laço de repetição:
ip = 0
for ip in range(1,255):
    print ("Varrendo IP: 192.168.0.%s" %ip)

#Trabalhando com condições:
if len(sys.argv) <= 2:
        print("Modo de uso: ./argv.py IP PORTA")

else:   
    print("Varrendo o host: ",sys.argv[1], "Na porta: ",sys.argv[2])
    
#O comando chama a função do sistema operacional
os.system("netstat -nlpt")