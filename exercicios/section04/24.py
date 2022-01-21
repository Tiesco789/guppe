# Leia um valor de área em metros quadrados e apresente-o convertido em acres.
# A formula de conversão é: A = M * 0.000247
M = float(input("Digite um valor em m²: "))
A = M * 0.000247
print("O valor em m² para acres é: %0.6f" % A)
