# Faça um programa que leia o valor de um produto e imprima o valor com desconto,
# tendo em vista que o desconto foi de 12%

produto = float(input("Digite o valor do produto: "))

desconto = produto - (0.12 * 100)

print(f"O valor final do produto é: {desconto}")
