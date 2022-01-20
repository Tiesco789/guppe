"""
Conjuntos
— Conjunto em qualquer linguagem de programação, estamos fazendo referência à teoria de conjuntos da matemática
— Aqui no Python, os conjuntos são chamados de sets

Dito isto, da mesma forma que na matemática:
— Sets (conjuntos) não possuem valores duplicados;
— Sets (conjuntos) não possuem valores ordenados;
— Elementos não são acessados via índice, ou seja, conjuntos não são indexados;

Conjuntos são bons para se utilizar quando precisamos armazenar elementos mas não nos importamos com a ordenaçào deles.
Quando não precisamos se preocupar com chaves, valores e itens duplicados

Os conjuntos (sets) são referenciados em python com chaves {}

Diferença entre conjutnos (sets) e mapas (dicionários) em python:
    — Um dicionário tem chave/valor
    — Um conjunto tem apenas valor

# Definindo um conjunto
# Forma 1
s = set({1, 2, 3, 4, 5, 6, 7, 2, 3})  # Repare que temos valores repetidos
print(s)
print(type(s))

# OBS: Ao criar uim conjunto, caso seja adicionado um valor já existente, o mesmo será ignorado sem gerar error e nào fará parde do conjunto

# Forma 2
s = {1, 2, 3, 4, 5, 5}
print(s)
print(type(s))

# Podemos verificar se um determinado valor está contido em um conjunto

if 3 in s:
    print('Encontrei o valor 3')
else:
    print('Não encontrei o valor 3')

# Importante lembrar que, alem de não termos valores duplicados, os valores não são ordenados

dados = 99, 2, 34, 23, 2, 12, 1, 44, 5, 34

# Listas aceitam valores duplicados, então temos 10 elementos
lista = list(dados)
print(f"Lista: {lista} com {len(lista)} elementos")

# Tuplas aceitam valores duplicados, então temos 10 elementos
tupla = tuple(dados)
print(f"Tupla: {tupla} com {len(tupla)} elementos")

# Dicionários não aceitam chaves duplicadas, então temos 8 elementos
dicionario = {}.fromkeys(dados, 'dict')
print(f"Dicionário: {dicionario} com {len(dicionario)} elementos")

# Conjuntos não aceitam valores duplicados, então temos 8 elementos
conjunto = set(dados)
print(f"Conjunto: {conjunto} com {len(conjunto)} elementos")

# Assim como os outros conjuntos python, podemos colocar tipos de dados misturados em Sets
s = {1, 'b', True, 1.23, 44}
print(s)
print(type(s))

# Podemos iterar em um set normalmente
for valor in s:
    print(valor)

# Usos interessantes com sets
# Imagine que fizemos um formulário de cadastro de visitantes em uma feira ou museu,
# os visitantes informam manualmente a cidade de onde vieram
# Nós adicionamos cada cidade em uma lista Python, já que em uma lista podemos adicionar novos elmentos e ter repetições

cidades = ['Belo Horizante', 'São Paulo', 'Campo Grande',
           'Cuiaba', 'Campo Grande', 'São Paulo', 'Cuiaba']
print(cidades)
print(len(cidades))

# Agora precisamos saber quantas cidades distintas, ou seja, únicas, temos.
# O que você faria? Faria um loop na lista?
# Podemos utilizar o set para isso
print(len(set(cidades)))

s = {1, 2, 3}
s.add(4)
print(s)

s = {1, 2, 3}
s.remove(3)
print(s)

s.discard(2)
print(s)

# Copiando um conjunto para outro
# Forma 1 - Deep Copy
novo = s.copy()
print(novo)

novo.add(4)

print(novo)
print(s)

# Forma 2 - Shallow Copy
novo = s
novo.add(4)
print(novo)
print(s)

s = {1, 2, 3}
print(s)

s.clear()
print(s)

# Precisamos gerar qum conjunto com nomes de estudantes únicos

# Forma 1 - Utilizando union
# unicos1 = estudantes_python.union(estudantes_java)
# print(unicos1)

# Forma 2 - Utilizando o | pipe
unicos2 = estudantes_python | estudantes_java
print(unicos2)

# Gerar um conjunto de estudantes que estão em ambos os cursos

# Forma 1 - Utilizando union
ambos1 = estudantes_python.intersection(estudantes_java)
print(ambos1)

# Forma 2 - utilizando o &
ambos2 = estudantes_python & estudantes_java
print(ambos2)

# Métodos matemáticos de conjuntos
# Imagine que temos dois conjuntos: um contendo estudantes do curso Python e um
# Contendo estudantes do curso Java

estudantes_python = {'Pedro', 'Maria', 'Cláudia', 'João', 'Marcos', 'Patricia'}
estudantes_java = {'Ana', 'Maria', 'Cláudia', 'João', 'Marcos', 'Patricia'}

# Veja que alguns alins que estudam python também estudam java.
# Gerar um conjunto de estudantes que não estão no outro curso

so_python = estudantes_python.difference(estudantes_java)
print(so_python)

so_java = estudantes_java.difference(estudantes_python)
print(so_java)


"""
