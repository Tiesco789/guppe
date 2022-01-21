# Leia um angulo em radianos e apresente-o convertido em graus.
# A formula de conversão é: G = R * 180 / PI

import math

R = float(input("Digite um angulo em radianos: "))
G = R * 180 / math.pi
print("O angulo em graus é: %0.2f" % G)
