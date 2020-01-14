import socket

HOST = "0.0.0.0"
PORT = 65432

strToSend = ""

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#AF_INET = IPv4
#SOCK_STREAM = TCP

s.bind((HOST, PORT))

while True:
    data, address = s.recvfrom(4096)
    print("Messaggio ricevuto dal client " + str(address) + ": " + data.decode())

    if(str(data) == "stop"):
        break

    #text = input("Inserisci risposta: ")
    #s.sendto(text.encode(), address)

s.close()
print("Connessione chiusa")
