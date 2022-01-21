# Leia um valor em real e a cotação do dolar.
# Em seguida, imprima o valor correspondente em dólares
# dolarQtd = float(input("Digite uma quantidade em dolares: "))
realQtd = float(input("Digite um valor em reais: "))
cotacaoDolar = float(input("Digte a cotação do dolar atual: "))
convert = realQtd / cotacaoDolar
print("quantidade em dolares: %0.2f" % convert)
