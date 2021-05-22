"""
List Comprehension

- Utilizando List Comprehension nós podemos gerar novas listas com dados processados a partir de outro iterável.

# Sintax 

[ dado for dado in iterável ]
"""

# Exemplos

numeros = [1, 2, 3, 4, 5]

res = [n * 10 for n in numeros]

print(res)

"""
Para entender melhor o que está acontecendo, devemos dividir a expressão em duas partes:

- A primeira parte: for n in numeros
- A segunda parte: n * 10

"""

res = [n / 2 for n in numeros]

print(res)

def funcao(valor):
    return valor*valor

res = [funcao(n) for n in numeros]

print(res)

# Lista vs loop
# Loop
# 
 
numeros_dobrados = []
for n in [1, 2, 3, 4, 5]:
    numeros_dobrados.append(n*2)

print(numeros_dobrados)

# Lista

print([n * 2 for n in [1, 2, 3, 4, 5]]) #Python avançado!


# Exemplo

nome = 'Geek University'

print([letra.upper() for letra in nome])

# 2

def caixa_alta(nome):
    nome = nome.replace(nome[0], nome[0].upper())
    return nome

amigos = ['maria', 'julia', 'pedro', 'guilherme', 'vanessa']

print([caixa_alta(amigo) for amigo in amigos])

# 3 

print([numero * 3 for numero in range(1, 10)])

# 4

print([bool(valor) for valor in [0, [], '', True, 1, 3.14]])