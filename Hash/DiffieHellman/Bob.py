import socket as sck

s = sck.socket(sck.AF_INET, sck.SOCK_STREAM)
s.bind(("0.0.0.0", 9999))
s.listen()

conn, address = s.accept()

N = 53923
g = 546

A = int(conn.recv(4096).decode())

b = int(input(f"Inserisci un numero compreso tra 1 e {N}\n>>>"))

B =(g**b) % N

print(f"B= {B}")

conn.sendall(str(B).encode())

K =(A**b) % N
print(f"K= {K}")
conn.close()
s.close()