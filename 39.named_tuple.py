"""
Módulo Collections - Named Tuple

# Recap tupla

tuple = (1, 2, 3)
print(tuple[1])

Named Tuple -> São tuplas, diferenciadas, onde, especificamos um nome para a mesma e também parâmetros
"""
# Import

from collections import namedtuple

# Precisamos definir o (nome, parâmetros)

# Forma 1 - declaração namedtuple

cachorro = namedtuple('cachorro', 'idade raça nome')


# Forma 2 - declaração namedtuple

cachorro = namedtuple('cachorro', 'idade, raca, nome')


# Forma 3 - declaração namedtuple

cachorro = namedtuple('cachorro', ['idade', 'raca', 'nome'])

# Usando

ray = cachorro(idade = 2, raca = 'Chow Chow', nome = 'Ray')


print(ray)

# Forma 1

print(ray[0]) # idade
print(ray[1]) # raca
print(ray[2]) # nome

# Forma 2

print(ray. idade) #idade
print(ray. raca) # raca
print(ray. nome) # nome

print(ray.index('Chow Chow'))
print(ray.count('Chow Chow'))
