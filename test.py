A, B, C = input().split(" ")
A, B, C = int(A), int(B), int(C)

X = A - B
maior_ini = int((A + B + abs(X)) / 2)

Y = maior_ini - C
maior_fin = int((maior_ini + C + abs(Y)) / 2)

print(f"{maior_fin} eh o maior")
