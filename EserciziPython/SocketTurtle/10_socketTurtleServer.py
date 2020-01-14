import socket
import turtle

HOST = "0.0.0.0"
PORT = 65432
strToSend = ""

turtle.color("red","red")
turtle.speed(1)

distanza = 50

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#AF_INET = IPv4
#SOCK_STREAM = TCP

s.bind((HOST, PORT))
s.listen()
conn, addr = s.accept()
print("\nSi è connesso: ", addr)

while True:
    data = conn.recv(4096)

    print("Messaggio ricevuto dal client: ", data.decode())

    if data.decode() == "0":
            break
    if not (data.decode() in ["a", "i", "d", "s"]):
        strToSend = "\nInput non valido, il comando deve essere a(avanti), i(indietro), d(destra) o s(sinistra)"
        conn.sendall(strToSend.encode())
    else:
        if(len(data.decode()) > 1):
            for k in range(0, len(data.decode())):
                if(data.decode()[k] == "a"):
                    turtle.forward(distanza)
                    strToSend = "\n> turtle -> avanti, coordinate: , X: " + str(turtle.xcor()) + " Y: " + str(turtle.ycor())
                    conn.sendall(strToSend.encode())
                elif(data.decode()[k] == "i"):
                    turtle.backward(distanza)
                    strToSend = "\n> turtle -> indietro, coordinate: , X: " + str(turtle.xcor()) + " Y: " + str(turtle.ycor())
                    conn.sendall(strToSend.encode())
                elif(data.decode()[k] == "d"):
                    turtle.right(90)
                    strToSend = "\n> turtle -> gira a destra, coordinate: , X: " + str(turtle.xcor()) + " Y: " + str(turtle.ycor())
                    conn.sendall(strToSend.encode())
                elif(data.decode()[k] == "s"):
                    turtle.left(90)
                    strToSend = "\n> turtle -> gira a sinistra, coordinate: , X: " + str(turtle.xcor()) + " Y: " + str(turtle.ycor())
                    conn.sendall(strToSend.encode())
        else:
            if(data.decode() == "a"):
                turtle.forward(distanza)
                strToSend = "\n> turtle -> avanti, coordinate: , X: " + str(turtle.xcor()) + ", Y: " + str(turtle.ycor())
            elif(data.decode() == "i"):
                turtle.backward(distanza)
                strToSend = "\n> turtle -> indietro, coordinate: , X: " + str(turtle.xcor()) + ", Y: " + str(turtle.ycor())
            elif(data.decode() == "d"):
                turtle.right(90)
                strToSend = "\n> turtle -> gira a destra, coordinate: , X: " + str(turtle.xcor()) + ", Y: " + str(turtle.ycor())
            elif(data.decode() == "s"):
                turtle.left(90)
                strToSend = "\n> turtle -> gira a sinistra, coordinate: , X: " + str(turtle.xcor()) + ", Y: " + str(turtle.ycor())

            conn.sendall(strToSend.encode())

turtle.done()
s.close()
print("Connessione chiusa")