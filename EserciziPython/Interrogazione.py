import turtle as t

print("Inserire una sequenza contenete solo le lettere f, b, r, l")
sequenza = input()

t.color("red","red")
t.speed(1)

distanza = 50

k = 0

for carattere in sequenza[5:]:
    if(carattere == "f"):
        t.forward(distanza)
    elif(carattere == "b"):
        t.backward(distanza)
    elif(carattere== "r"):
        t.right(90)
    elif(carattere == "l"):
        t.left(90)
    else:
        print("La sequenza contiene una lettera non supportata")
t.done()