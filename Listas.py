"""
# Podemos facilmente checar se determinado valor está contido na lista
num = 7
if num in lista4:
    print(f'Encontrei o número {num}')
else:
    print(f'Não encontrei o número {num}')

# Podemos facilmente ordernar uma lista
lista1.sort()
print(lista1)

# Podemos facilmente contar o número de ocorrências de um valor em uma lista\
print(lista1.count(1))
print(lista5.count('e'))

Adcionar elementos em listas
Para adicionar elementos em listas, utilizamos a função append
OBS: Com append, nós só conseguimos adicionar um elemento por vez

print(lista1)
lista1.append(42)
print(lista1)

lista1.append([8, 3, 1])  # Coloca a lista como elemento único (sublista)
print(lista1)

if [8, 3, 1] in lista1:
    print('encontrei a lista')
else:
    print('Não encontrei a lista')

lista1.extend([123, 44, 67])  # Coloca cada elemendo da lista como valor adicional à lista
print(lista1)

# Podemos inserir um novo elemento na lista informando a posição do índice
# OBS: Isso não substitui o valor inicial. o mesmo será deslocado para a direita da lista
lista1.insert(2, 'Novo valor')
print(lista1)

# Podemos facilmente juntar duas listas
lista1 = lista1 + lista2
# lista1.extend(lista2)
print(lista1)

# Podemos facilmente inverter uma lista
# Forma 1
# lista1.reverse()
# lista2.reverse()

# Forma 2
print(lista1[::-1])
print(lista2[::-1])

# Copiar lista
lista6 = lista2.copy()
print(lista6)

# Podemos contar quantos elementos tem em uma lista
print(len(lista5))

# Podemos remover facilmente o ultimo elemento de uma lista
# OBS: O pop não somente remove o ultimo elemento mas também o retorna
print(lista5)
lista5.pop()
print(lista5)

# Podemos remover um elemento pelo indice
# OBS: Os elementos à direita deste indice sao deslocado para a esquerda
# OBS: Se não houver elemento no indice informando, teremos erro
lista5.pop(2)
print(lista5)

# podemos remover todos os elementos da lista
print(lista5)
lista5.clear()
print(lista5)

# Podemos facilmente elementos em uma lista
nova = [1, 2, 3]
print(nova)
nova = nova * 3
print(nova)

# Podemos facilmente converter uma string para uma lista
# Exemplo 1
curso = 'Programação em python: essencial - Ex1'
print(curso)
curso = curso.split()
print(curso)

# OBS: Por padrão o split separa os elementdo da lista pelo espaço entre elas.

# Exemplo 2
curso = 'Programação,em,python:,essencial,Ex2'
print(curso)
curso = curso.split(',')
print(curso)

# Abaixo estamos falando: pega a lista6, coloca um caracter entre cada elemento e transforma em uma string
curso = ' '.join(lista6)
print(curso)

curso = '$'.join(lista6)
print(curso)

# Podemos realmente colocar qualquer tipo de dado em uma lista, inclusive misturando esses dados
lista6 = [1, 2.34, True, 'Geek', 'd', [1, 2, 3], 4654654654]

# Iterand sobre lista
#Ex1: Utilizando For
soma = 0

for elemento in lista4:
    print(elemento)
    soma = soma + elemento

print(soma)

# Ex2: Utilizando while
carrinho = []
produto = ''

while produto != 'sair':
    print("Adicione um produto na lista ou digite 'sair' para sair: ")
    produto = input()
    if produto != 'sair':
        carrinho.append(produto)

for produto in carrinho:
    print(produto)


# Fazemos o acesso aos elementso de forma indexada
cores = ['verde', 'amarelo', 'azul', 'branco']
print(cores[0])
print(cores[1])
print(cores[2])
print(cores[3])

# Fazer acesso aos elementos de forma inversa
# Para entender melhor o indice negativo,
# pense na lista como um circulo onde o final de um elemento está ligado ao incio da lista
print(cores[-1])
print(cores[-2])
print(cores[-3])
print(cores[-4])

for cor in cores:
    print(cor)

indice = 0
while indice < len(cores):
    print(cores[indice])
    indice = indice + 1



# Gerar indice em um for
for indice, cor in enumerate(cores):
    print(indice, cor)


# Listas aceitam valores repetidos
lista = []
lista.append(42)
lista.append(42)
lista.append(33)
lista.append(33)
lista.append(42)
print(lista)

# Outros métodos não tão importantes mas também uties
# Econtrar o indice de um elemento na lista

numeros = [5, 6, 7, 5, 8, 9, 10]

# Em qual indice da lista está o valor 6?
print(numeros.index(6))

# Em qual indice da lista está o valor 9?
print(numeros.index(9))

# OBS: Caso não tenha esse elemento na lista, será apresentado erro

# OBS: retorna o indice do primeiro elemento encontrado
print(numeros.index(5))

# Podemos fazer busca dentro de um range, ou seja, qual indice começar a buscar
print(numeros.index(5, 1))
print(numeros.index(5, 2))
print(numeros.index(5, 3))
# print(numeros.index(5, 4))
# OBS: Caso não tenha este elemento na lista, será apresentado erro valueError

# Podemos fazer busca dentro de um range, inicio/fim
print(numeros.index(8, 3, 6))

# Revisando de slicing
# lista[inicio:fim:passo]
# range(inicio:fim:passo)

# Trabalhando com slice de lista com o parametro 'inicio'

lista = [1, 2, 3, 4]
print(lista[1:])
print(lista[:2])
print(lista[:4])
print(lista[1:3])
print(lista[1::2])
print(lista[::2])

# Soma, valor maximo, valor minimo, tamanho
# se os valores forem todos inteiros ou reais
lista = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]
print(sum(lista))
print(max(lista))
print(min(lista))
print(len(lista))


lista = [1, 2, 3, 4, 5, 6]
print(lista)
print(type(lista))

tupla = tuple(lista)
print(tupla)
print(type(tupla))

# Desempacotamento de listas
# OBS: Se tivermos mais elementos para desempacotar do que variaveis para receber valores, teremos ValueError
lista = [1, 2, 3]
num1, num2, num3 = lista
print(num1)
print(num2)
print(num3)

# Copiando uma lista para outra (Shallow Copy, Deep copy
# Forma 1 - Deep Copy

lista = [1, 2, 3]
print(lista)

nova = lista.copy()
print(nova)

nova.append(4)

print(lista)
print(nova)
# Veja que ao utilizarmos lista.copy() copiamos os dados da lista para uma nova lista,
# mas elas ficaram totalmente indepentendes, ou seja, modificando uma lista, não agfeta a outra.
# Isso em python é chamado de deep copy


type([])
lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]
lista2 = ['G', 'e', 'e', 'k', ' ', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']
lista3 = []
lista4 = list(range(11))
lista5 = list('Geek University')
cores = ['verde', 'amarelo', 'azul', 'branco']

# ---------------------------------------------------------------

# Forma 2 - Shallow Copy
lista = [1, 2, 3]
print(lista)

nova = lista
print(nova)
nova.append(4)

print(lista)
print(nova)
# Veja que utilizamos a cópiua via atribuição e copiamos os dados da lista p[ara uma lista, mas após realizar
# modificação em uma das listas, essa modificação se refletiu em amas as listas
# Isso em python é chamado de Shallow Copy
"""
