# Leia uma temperatura em graus Fahrenheit e apresente-a convertida em graus Celsius.
# A formula de conversão é C = 5.0 * (F - 32) / 9.0, sendo C a temperatura em Celsius e F a temperatura em Fahrenheit.

F = float(input("Digite a temperatura em Fahrenheit: "))
C = 5.0 * (F - 32) / 9.0
print(f"A temperatura em Celsius é: {C}")
