import socket

#função socket, da classe socket:
#Os parâmetro são familia A_INET, que significa IPV4
##E o tipo. que pode ser:
#O SOCK_STREAM = tcp
#O SOCK_DGRAM = UDP
servidor = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#Bind é o endereço, se a familia for do tipo AF_INET os paramêtros precisam
# ser o (host,porta)

servidor.bind(('',12000)) #host = própria máquina

# loop para fficar sempre à escuta
while True:
	#recvfrom parametro é o tamanho do buffer de recebimento, aconselhado 2048
	#recebe mensagem em bytes e endereço
	mensagem_bytes, endereco_ip_client = servidor.recvfrom(2048)

	#converte a mensagem em bytes e conevrte para string
	mensagem_resposta = mensagem_bytes.decode()

	mensagem_confirma = "Imprimi a hora"
	#envia mensagem de confirmação em bytes para o endereço do cliente
	servidor.sendto(mensagem_confirma.encode(),endereco_ip_client)

	#imprime a hora
	print(mensagem_resposta)
#-----------------------------------------------------------------
