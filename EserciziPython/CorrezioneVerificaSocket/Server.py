import socket

HOST = "0.0.0.0"
PORT = 54321

lista = []

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((HOST, PORT))

while True:
    print("\n-----------------------------\n")
    inserito = False
    data, address = s.recvfrom(4096)
    data = data.decode()

    if data == "":
        break

    if data[0:6] == "SCORE ":
        cont = 0
        k = 7
        while data[k] != ",":
            cont = cont + 1
            k = k + 1
        giocatore = data[6:(7+cont)]
        giocatore = giocatore.upper()
        punteggio = data[(9+cont):len(data)]
        if lista == []:
            lista.append([giocatore, punteggio])
            inserito = True
        else:
            for k in lista:
                if k[0] == giocatore:
                    k[1] = punteggio
                    inserito = True
            if inserito == False:
                lista.append([giocatore, punteggio])
                inserito = True

        if inserito == True:
            for k in lista:
                print(k)

s.close()