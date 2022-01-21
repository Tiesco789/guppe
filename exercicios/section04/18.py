# Leia um valor de volume em metros cubicos e apresente-o convertido litros.
# A fórmula de conversão é: L = 1000 * M
M = float(input("Digite um valor em metros cubicos: "))
L = 1000 * M
print("A conversão para litros é: %0.2f" % L)
