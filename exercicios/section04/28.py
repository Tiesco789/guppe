# Faça a leitura de tres valores e apresente como resultado a soma dos quadrados dos tres valores lidos.

valor1 = int(input("Valor: "))
valor2 = int(input("Valor: "))
valor3 = int(input("Valor: "))

result = pow(valor1, 2) + pow(valor2, 2) + pow(valor3, 2)

print(f"O resultado da soma dos tres valores é: {result}")
