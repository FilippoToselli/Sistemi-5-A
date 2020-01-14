from turtle import *

a = 0
b = 1
color("red", "blue")

print("Inserire il numero di braccia: ")
braccia = int(input())

while True:
    forward(b)
    a, b = b, a + b
    left(90)
    braccia = braccia - 1
    if(braccia == 0):
        break
done()