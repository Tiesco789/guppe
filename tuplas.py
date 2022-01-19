"""
Tuplas ou tuples
Tuplas são bastante paracidas com listas.
existem basicamente duas diferenças básicas:

1 - As tuplas são representadas por parentêses ()

2 - As tuplas são imutaveis: Isso significa que ao se criar uma tupla ela não muda.
Toda operação em uma tupla gera uma nova tupla


# CUIDADO 1: As tuplas são representadas por (), mas veja:
tupla1 = (1, 2, 3, 4, 5, 6)
print(tupla1)
print(type(tupla1))

tupla2 = 1, 2, 3, 4, 5, 6
print(tupla2)
print(type(tupla2))

# Cuidado 2: Tuplas com 1 elemento
tupla3 = (4)  # Isso não é uma tupla
print(tupla3)
print(type(tupla3))

tupla4 = (4,)  # Isso é uma tupla
print(tupla4)
print(type(tupla4))

tupla5 = 4,  # Isso é uma tupla
print(tupla5)
print(type(tupla5))

# Conclusão: Podemos concluir que as tuplas são definidas pela vírgula e não pelo uso do parenteses
EX:
(4)     -> Não é uma tupla
(4,)    -> É uma tupla
4,      -> É uma tupla

# Podemos gerar uma tupla dinamicamente com range (inicion, fim, passo)
tupla = tuple(range(11))
print(tupla)
print(type(tupla))


# Desempacotamento de tupla
tupla = ('Geek University', 'Programação em Python: Essencial')
escola, curso = tupla
print(escola)
print(curso)
# OBS: Gera erro (ValueError) se colocarmos um número diferente de elementos para desempacotar

# Métodos para adição e remoção de elementos nas tuplas não existem, dado o fato das tuplas serem imutáveis
# soma, valor máximo, valor minimo, tamanho
# se os valores forem todos inteiros ou reais
tupla = (1, 2, 3, 4, 5, 6)
print(sum(tupla))
print(max(tupla))
print(min(tupla))
print(len(tupla))

# Concateneção de tuplas
tupla1 = (1, 2, 3)
print(tupla1)

tupla2 = (4, 5, 6)
print(tupla2)

print(tupla1 + tupla2)  # Tuplas são imutavéis
print(tupla1)
print(tupla2)

tupla1 = tupla1 + tupla2  # Tupla são imutavéis, mas podemos sobrescrever seus valores
print(tupla1)

# Verificar se determinado elemento está contido na tupla
tupla = (1, 2, 3)
print(3 in tupla)

# Iterando sobre uma tupla
tupla = (1, 2, 3)
for n in tupla:
    print(n)

for indice, valor in enumerate(tupla):
    print(indice, valor)

# Contando elementos dentro de uma tupla
tupla = ('a', 'b', 'c', 'd', 'e', 'a', 'b')
print(tupla.count('c'))

escola = tuple('Geek University')
print(escola)

print(escola.count('e'))

# Dicas na utlização de tuplas
# Devemos utilizar tuplas sempre que não precisarmos modificar os dados contidos em uma coleção
# Ex: 1
meses = ('Janeiro', 'Fevereiro', 'Maço', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')

# O acesso a elementos de uma tupla também é semelhante a de uma lista
print(meses[5])

# Iterar com while
i = 0
while i < len(meses):
    print(meses[i])
    i = i + 1

print(meses.index('Junho'))

# Slicing
# Tulpa[inicio:fim:passo]
print(meses[5:9])

# Por que utilizar Tuplas?
# 1 - Tuplas são mais otimizadas do que listas
# 2 - Tuplas deixam seu código mais seguro
# Isso porque trabalhar com elementos imutaveis traz segurança para o código.

# Copiando uma tupla para outra
tupla = (1, 2, 3)
print(tupla)

nova = tupla
print(nova)
print(tupla)

outra = (4, 5, 6)

nova = nova + outra
print(nova)
print(outra)

"""

