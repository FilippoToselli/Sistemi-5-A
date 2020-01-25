import socket as sck

s = sck.socket(sck.AF_INET, sck.SOCK_STREAM)
s.bind(("0.0.0.0", 9999))
s.listen()

conn, address = s.accept()

N = 103782176851
g = 987654321

A = int(conn.recv(4096).decode())

b = int(input(f"Inserisci un numero compreso tra 1 e {N}\n>>>"))

B =(g**b) % N

conn.sendall(str(B).encode())

K =(A**b) % N
print(f"K= {K}")
conn.close()
s.close()