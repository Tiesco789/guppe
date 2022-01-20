# Leia uma temeperatura em graus Celsius e apresente-a convertida em graus Fahrenheit.
# A formula de conversão é F = C * (9.0 / 5.0) + 32.0, sendo F a temperatura em Fahrenheit e C a temperatura em Celsius.

C = float(input("Digite a temperatura em Celsius: "))
F = C * (9.0 / 5.0) + 32
print(f"A temperatura em Fahrenheit é: {F}")
