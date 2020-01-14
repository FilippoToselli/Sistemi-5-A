import socket

HOST = "192.168.0.96"
PORT = 1234
strToSend = ""

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#AF_INET = IPv4
#SOCK_STREAM = TCP

s.connect((HOST, PORT))

while True:
    strToSend = input("\n> Stringa da inviare ('exit' per uscire): ")
    s.sendall(strToSend.encode())
    if strToSend == "exit":
       break
    data = s.recv(4096)
    print("\nMessagio ricevuto dal server: ", data.decode())
    if data.decode() == "exit":
      break
s.close()
print("Connessione chiusa")