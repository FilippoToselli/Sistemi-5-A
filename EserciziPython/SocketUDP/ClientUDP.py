import socket

SERVER = "127.0.0.1"
PORT = 65432

strToSend = ""

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#AF_INET = IPv4
#SOCK_STREAM = TCP

while True:
    testo = input("Inserisci il messaggio: ")
    s.sendto(testo.encode(), (SERVER, PORT))

    if(str(testo) == "stop"):
        break

    #data, server = s.recvfrom(4096)
    #print("Messaggio ricevuto dal server " + str(server) + " : " + data.decode())

s.close()
print("Connessione chiusa")