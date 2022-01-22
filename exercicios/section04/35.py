# Sejam a e b os catetos de um triangulo, onde a hipotenusa é obtida pela equação:
# hipotenusa = raizQuadrada(a² + b²).
# Faça um programa que receba os valores de a e b e calcule o valor da hipotenusa através da equação.
# Imprima o resultado dessa operação

import math

A = float(input("Digite um valor do cateto A: "))
B = float(input("Digite um valor do cateto B: "))

hip = math.sqrt(pow(A, 2) + pow(B, 2))

print(f"O valor da hipotenusa é: {hip}")
