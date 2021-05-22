"""
Set Comprehension

Lista = [1, 2, 3, 4, 5]
Set = {1, 2, 3, 4, 5}
Tupla = (1, 2, 3, 4, 5)

"""

# Exemplo

numeros = {num for num in range(1, 7)}
print(numeros)

# Exemplo

numeros = {x: x ** 2 for x in range(10)}
print(numeros)

