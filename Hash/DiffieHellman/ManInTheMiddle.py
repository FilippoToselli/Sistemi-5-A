N = 53923
g = 546

A = #inserire A output Alice
B = #inserire B output Bob

for a in range(1, N):
    if ((g**a) % N) == A:
        print (f"a= {a}")

for b in range(1, N):
    if((g**b) % N) == B:
        print(f"b= {b}")