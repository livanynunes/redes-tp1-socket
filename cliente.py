
import socket
from calendar import*;
from time import*;

cliente = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

while True:
	#Data e hora testes

	#print(time())
	#print (localtime(time()))
	#print(asctime(localtime(time())))

	mensagem_envio = asctime(localtime(time()))
	#print(mensagem_envio)

	#mensagem_envio = input("digitar qqqualque coisa: ")

	cliente.sendto(mensagem_envio.encode(),("172.17.0.1",12000))

	mensagem_bytes, endereco_ip_servidor = cliente.recvfrom(2048)
	print(mensagem_bytes.decode())


