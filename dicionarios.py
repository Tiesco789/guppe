"""
Dicionários
OBS: em algumas linguagens, os dicionários Python são conhecidos por mapas.
Dicionários são coleções do tipo chave/valor

Dicionarios são representados por chaves {}

OBS: Sobre dicionários:
    — Chave e valor são representados por dois pontos 'chave: valor'
    — Tanto chave quanto valor podem ser de qualquer tipo de dado
    — Podemos misturar tipos de dados

print(type({}))

# Forma 1 (Mais comum)
paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}
print(paises)

# Forma 2 (Menos comum)
paises = dict(br='Brasil', eua='Estados Unidos', py='Paraguai')
print(paises)

# Acessando elementos
# Forma 1 — Acessando via chave, da mesma forma que lista/tupla
print(paises['br'])
# print(paises['py'])

# OBS: Caso tentamos fazer um acesso utilizando uma chave que não existe, teremos o erro KeyError

# Forma 2 — Acessando via get — Recomendada
print(paises.get('br'))
print(paises.get('ru'))

# Caso o get não encontre o objeto com a chave informada será retorando o valor None e não sera gerado KeyError
pais = paises.get('ru')

if pais:
    print(f'Encontrei o país {pais}')
else:
    print('Não encontrei o país')

# Podemos definir um valor padrão para caso não encontremos o objeto com a chave informada
pais = paises.get('ru', 'Não encontrado')

print(f'Não Encontrei país {pais}')


# Podemos verificar se determinada chave se encontra em um dicionário
print('br' in paises)
print('ru' in paises)
print('Estados Unidos' in paises)

if 'ru' in paises:
    russia = paises['ru']


# Podemos utilizar qualquer tipo de dado, inclusive listas, tuplas, dicionarios como chaves de dicionarios

# Tuplas são interessantes de serem usadas como chaves de dicionarios por serem imutaveis
localidades = {
    (35.6895, 39.6917): 'Escritorio em Tókio',
    (40.7128, 74.0060): 'Escritorio em Nova York',
    (37.7749, 122.4194): 'Escritorio em São Paulo',
}

print(localidades)

# Adicionar elementos em um dicionário
receita = {'jan': 100, 'fev': 120, 'mar': 300}
print(receita)

# Forma 1
receita['abr'] = 350
print(receita)

# Forma 2
novo_dado = {'mai': 500}
receita.update(novo_dado)
print(receita)

# Atualizando dados em um dicionário
# Forma 1
receita['mai'] = 550
print(receita)

# Forma 2
receita.update({'mai': 600})
print(receita)

# CONCLUSÃO 1: A forma de adicionar novos elementos ou atualizar dados em um dicionáirio é a mesma
# CONCLUSÃO 2: Em dicionarios, não podemos ter chaves repetidas.

# Remover dados de um dicionario
receita = {'jan': 100, 'fev': 120, 'mar': 300}
print(receita)

# Forma 1 — Mais comum
ret = receita.pop('mar')
print(ret)
print(receita)

# OBS 1: Aqui precisamos SEMPRE informar a chave, e caso não encontre o elemnto, um KeyError é retornado
# OBS 2: Ao removermos um objeto, o valor deste objeto é sempre retornado

# Forma 2
del receita['fev']
print(receita)

# Se a chave não existir, um KeyError é retornado
# OBS: Neste caso o valor removeido não é retornado
"""

# Imagine que você tem um comércio eletronico, onde temos um carrinho de compras, e temos que saber qual o valor total de todos os produtos.
"""
Carrinho de compras:
    Produto 1:
        - Nome
        - Quantidade
        - Preço
    Produto 2:
        - Nome
        - Quantidade
        - Preço

# 1 - poderiamos utilizar uma lista para isso? sim
carrrinho = []
produto1 = ['Playstation 4', 1, 2300.00]
produto2 = ['God of War 4', 1, 150.00]

carrrinho.append(produto1)
carrrinho.append(produto2)

print(carrrinho)

# Teriamos que saber qual é o indice de cada informação no produto

# 2 - Poderiamos utilizar uma tupla para isso? sim
produto1 = ['Playstation 4', 1, 2300.00]
produto2 = ['God of War 4', 1, 150.00]

carrinho = (produto1, produto2)
print(carrinho)

# 3 - Poderiamos utilizar um dicionário para isso? sim
carrinho = []
produto1 = {'nome': 'Playstation 4', 'quantidade': 1, 'preco': 2300.00}
produto2 = {'nome': 'God of War 4', 'quatidade': 1, 'preco': 150.00}

carrinho.append(produto1)
carrinho.append(produto2)
print(carrinho)

# Desta forma, facilmente adicionamos ou removemos produtos no carrinho e em cada produto
# Podemos ter a certeza sobre cada informação.

# Método de dicionário
d = dict(a=1, b=2, c=3)
print(d)
print(type(d))

# Limpar o dicionário
d.clear()
print(d)

# Copiando um dicionário para outro
# Forma 1 - Deep Copy
novo = d.copy()
print(novo)

novo['d'] = 4
print(d)
print(novo)

# Forma 2 - shallow copy
novo = d
print(novo)

novo['d'] = 4
print(d)
print(novo)

# Forma não usual de criação de dicionários
outro = {}.fromkeys('a', 'b')
print(outro)
print(type(outro))

usuario = {}.fromkeys(['nome', 'pontos', 'email', 'senha'], 'desconhecido')
print(usuario)
print(type(usuario))

# O metodo fromkeys recebe dois parametros: um iterável e um valor.
# Ele vai gerar para cada valor do iteravel uma chave e irá atribuir a esta chave o valor informado

veja = {}.fromkeys('teste', 'valor')
print(veja)

veja = {}.fromkeys(range(1, 11), 'novo')
print(veja)

"""
