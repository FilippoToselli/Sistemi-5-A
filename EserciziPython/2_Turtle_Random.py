from turtle import *
import random as r

print("Inserire il numero di spostamenti")
scelta = input()

k = 0
spostamento = 20

speed(0)

for k in range(int(scelta)):
    if(r.random()>0.5):
        left(90)
        color("red", "red")
    else:
        right(90)
        color("blue", "blue")
    forward(spostamento)
done()