# Leia um valor de comprimento em polegadas e apresente-o convertido em centimetros.
# A formula de conversão é: C = P * 2.54

P = float(input("Digite um valor em polegadas: "))
C = P * 2.54
print("O valor convertido em CM é: %0.1f" % C)
