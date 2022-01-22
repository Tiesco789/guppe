# A importancia de R$780.000.00 será dividida entre tres ganhadores de um concurso
# sendo que da quantia total:
# - O primeiro ganhador receberá 46%
# - O segundo recebera 32%
# - O terceiro receberá o restante

premio = 780000.00

primeiro = premio * 0.46
segundo = premio * 0.32
terceiro = premio - primeiro - segundo

print(f"O ganhador 1 receberá: R${primeiro:.2f}")
print(f"O ganhador 2 receberá: R${segundo:.2f}")
print(f"O ganhador 3 receberá: R${terceiro:.2f}")
