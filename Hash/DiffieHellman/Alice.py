import socket as sck

s = sck.socket(sck.AF_INET, sck.SOCK_STREAM)
s.connect(("192.168.43.101", 65432))
print("connesso")

N = 103782176851
g = 987654321

a = int(input(f"Inserisci un numero compreso tra 1 e {N}\n>>>"))

A = g**a % N

s.sendall(str(A).encode())
B = int(s.recv(4096).decode())

K =(B**a) % N
print(f"K= {K}")
s.close()