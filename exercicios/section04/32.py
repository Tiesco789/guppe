# Leia um número inteiro e imprima a soma do sucessor de seu triplo com o antecessor de seu dobro
num = int(input("Digite um número inteiro: "))
antecessor = (pow(num, 2) - 1)
successor = (pow(num, 3) + 1)
print(
    f"Antecessor do seu dobro é: {antecessor}\nSucessor do seu triplo é: {successor}")
