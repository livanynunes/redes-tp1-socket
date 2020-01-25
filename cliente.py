import socket
from calendar import*;
from time import*;

#função socket, da classe socket:
#Os parâmetro são familia AF_INET, que significa IPV4
##E o tipo. que pode ser:
#O SOCK_STREAM = tcp
#O SOCK_DGRAM = UDP
cliente = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#Retorna string com data e horas atual, no formato
#p.e. Sun Apr 23 08:45:32 2019 - Dia da semana, mês, Dia do mês, hora, minutos, segundos e ano

mensagem_envio = asctime(localtime(time()))

#mensagem_envio = input("digitar qualque coisa: ") #se quiser receber mensagem do user

#cliente.sendto(mensagem_envio.encode(),("192.168.0.103",12000)) # rede de casa virada pra lua 2
cliente.sendto(mensagem_envio.encode(),("172.20.10.9",12000)) #meu celular rede

mensagem_bytes, endereco_ip_servidor = cliente.recvfrom(2048)

print(mensagem_bytes.decode())

#-----------------------------------------------------------------

