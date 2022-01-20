# Leia uma distancia em quilometros e apresente-a convertida em milhas.
# A formula de conversão é: M = K / 1.61

K = float(input("Digite uma velocidade em km/h: "))
M = K / 1.61
print("A velocidade em milhas é: %0.2f milhas" % M)
