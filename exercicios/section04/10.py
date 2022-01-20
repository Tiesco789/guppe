# Leia uma velocidade em km/h e apresente-a covertida em m/s. A fórmula de conversão é:
# M = K /3.6 sendo K a velocidade em km/h e M em m/s

Vel = float(input("Digite a velocidade em km/h: "))
M = Vel / 3.6
print("A velocidade em m/s é: %0.2f m/s" % M)
