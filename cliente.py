#!/usr/bin/python3

import socket
from calendar import*;
from time import*;

cliente = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

mensagem_envio = asctime(localtime(time()))

#mensagem_envio = input("digitar qualque coisa: ") #se quiser receber mensagem do user

#cliente.sendto(mensagem_envio.encode(),("192.168.0.103",12000)) # rede de casa virada pra lua 2
cliente.sendto(mensagem_envio.encode(),("172.20.10.9",12000)) #meu celular rede

mensagem_bytes, endereco_ip_servidor = cliente.recvfrom(2048)

print(mensagem_bytes.decode())

#-----------------------------------------------------------------

