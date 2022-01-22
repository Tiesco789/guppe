# Uma empresa contrata um encanador a R$30.00 por dia.
# Faça um programa que solicite o número de dias trabalhados pelo encanador e imprima a quantia líquida que deverá ser paga, sabendo-se que são descontados 8% para impostos de renda

valorDia = 30.00
diasTrabalhado = float(input("Quantos dias o encanador trabalho: "))
calc = valorDia * diasTrabalhado * 0.92
print(f"O Salário recebido é de: R${calc:.2f}")
9
