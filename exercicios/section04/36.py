# Leia a altura e o raio de um cilindro circular e imprima o volume do cilindro.
# O volume de um cilindro circular é calculado por meio da seguinte fórmula:
# V = pi * raio² * altura, onde pi é: 3.141592

altura = float(input("Digite o valor da altura: "))
raio = float(input("Digite o valor do raio: "))

pi = 3.141592

volume = pi * pow(raio, 2) * altura

print(f"O volume do círculo é de: {volume}")
