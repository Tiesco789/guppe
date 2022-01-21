# Leia um ângulo em graus e apresente-o convertido em radianos.
# A formula de conversão é : R = G * pi / 180

import math

G = float(input("Digite um angulo: "))
R = G * math.pi / 180
print("o angulo em radianos é: %0.2f" % R)
