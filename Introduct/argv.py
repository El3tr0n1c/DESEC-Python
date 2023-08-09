#!/usr/bin/python
import sys #trabalha com argumentos
import os #comandos do sistema operacional

#Dessa forma, você pode chamar o script já passando os argumentos (necessário importar sys)
#Exemplo: ./argv.py 192.168.0.1 80
print("Varrendo o host: ",sys.argv[1], "Na porta: ",sys.argv[2])

#O comando chama a função do sistema operacional
os.system("netstat -nlpt")