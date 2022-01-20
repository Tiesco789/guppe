# Leia uma velocidade em m/s e apresente-a convertida em km/h. A forumula de conversão é:
# k = m * 3.6 sendo m a velocidade em m/s e k em km/h

vel = float(input("Digite a velocidade em m/s: "))
k = vel * 3.6
print("A velocidade em km/h é: %0.2f km/h" % k)
