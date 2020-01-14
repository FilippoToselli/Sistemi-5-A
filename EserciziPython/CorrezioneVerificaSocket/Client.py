import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

HOST = "192.168.10.75"
PORT = 4884

NomeGiocatore = "Filippo"

while True:
    punteggio = str(input(">>>"))

    if punteggio == "":
        break

    testo = "SCORE " + NomeGiocatore + ", " + str(punteggio)
    s.sendto(testo.encode(), (HOST, PORT))

s.close()