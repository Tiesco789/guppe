# Leia o valor de um círculo e calcule e imprima a área do círculo correspondente.
# A área do círculo é: pi * raio², considere pi = 3.141592

raio = float(input("Digite o raio do círculo: "))
pi = 3.141592
resultado = pi * pow(raio, 2)
print(f"A área do circulo é: {resultado}")
