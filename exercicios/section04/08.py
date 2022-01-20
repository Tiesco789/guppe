from django import template

# Leia uma temperatura em graus Kelvin e apresente-a convertida em graus Celsius.
# A formula de conversão é C = K - 273.15, sendo C a temperatura em Celsius e K a temperatura em Kelvin.

K = float(input("Digite a temperatura em Kelvin: "))
C = K - 273.15
print(f"A temperatura em Kelvin é: {C}")
