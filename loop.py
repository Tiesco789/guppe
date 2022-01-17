"""
qtd = int(input('Quantas vezes esse loop deve rodar: '))
soma = 0

for n in range(1, qtd + 1):
    num = int(input(f"informe o {n}/{qtd} valor: "))
    soma = soma + num

print(f"A soma é {soma}")
"""

for _ in range(3):
    for num in range(1, 11):
        print('\U0001F605' * num)
