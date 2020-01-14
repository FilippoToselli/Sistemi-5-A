import turtle as t
import random as r

t.setup(800, 800)

nTurtles = 5

distanza = 800 / (nTurtles + 1)

l = []

cont = -400

t.speed(1)

for k in range (0,nTurtles-1):
    l.append(t.Turtle())
    l[k].penup()
    l[k].setx(-400)
    l[k].sety(cont + distanza)
    cont = cont + distanza
l.append(t)
t.penup()
t.setx(-400)
t.sety(cont + distanza)
cont = cont + distanza

uscita = True
while uscita:
    for i in range (0, nTurtles):
        l[i].forward(r.randrange(0, 21))
        if l[i].xcor() > 400:
            uscita = False
            print("Il vincitore è: ")
            print(i + 1)

t.done()