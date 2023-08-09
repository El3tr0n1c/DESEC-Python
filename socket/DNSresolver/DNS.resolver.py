#!/usr/bin/python

import sys,socket

#host = sys.argv[1]
print("DNS resolver de 3l3tr0n1c")
host = str(input("Digite o dominio: "))

print(host,"--->",socket.gethostname(host))

