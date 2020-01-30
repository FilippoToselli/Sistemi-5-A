import socket as sck

s = sck.socket(sck.AF_INET, sck.SOCK_STREAM)
s.connect(("127.0.0.1", 9999))
print("connesso")

N = 53923
g = 546

a = int(input(f"Inserisci un numero compreso tra 1 e {N}\n>>>"))

A = g**a % N

print(f"A= {A}")

s.sendall(str(A).encode())
B = int(s.recv(4096).decode())

K =(B**a) % N
print(f"K= {K}")
s.close()