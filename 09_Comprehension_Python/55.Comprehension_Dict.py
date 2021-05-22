"""
Dictionary Comprehension

Pense no seguinte:

Se quisermos criar uma lista, fazemos:

lista = [1, 2, 3 , 4]
tupla = (1, 2, 3 , 4) # 1, 2, 3, 4
conjunto = {1, 2, 3 , 4}

Se quisermos criar um dicionário

dicionario = {'a': 1,'b2': 2,'c': 3 ,'d': 4}

# SINTAXE

{chave: valor for valor in iterável}

- lista[valor for valor in iterável]
""" 

# EXEMPLO
"""
numeros = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

quadrado = {chave: valor ** 2 for chave, valor in numeros.items()}

print(quadrado)
"""


# EXEMPLO
"""
lista = [1, 2, 3, 4, 5]

quadrados = {valor: valor ** 2 for valor in lista}

print(quadrados)
"""
"""
chaves = 'abcde'
numeros = [1, 2, 3, 4, 5]

mistura = {chaves[i]:numeros[i] for i in range(0, len(chaves))}

print(mistura)
"""

# EXEMPLO

numeros = [1, 2, 3, 4, 5]

res = {num:('par' if num % 2 == 0 else 'impar') for num in numeros}

print(res)
