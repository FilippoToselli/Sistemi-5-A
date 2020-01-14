import turtle as t

print("Inserire una sequenza contenete solo le lettere f, b, r, l")
sequenza = input()

t.color("red","red")
t.speed(1)

distanza = 50

k = 0

for k in range(len(sequenza)):
    if(sequenza[k] == "f"):
        t.forward(distanza)
    elif(sequenza[k] == "b"):
        t.backward(distanza)
    elif(sequenza[k] == "r"):
        t.right(90)
    elif(sequenza[k] == "l"):
        t.left(90)
    else:
        print("La sequenza contiene una lettera non supportata")
t.done()