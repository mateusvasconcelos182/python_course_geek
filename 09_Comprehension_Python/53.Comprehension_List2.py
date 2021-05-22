"""
List Comprehension

Nós podemos adicionar estruturas condicionais lógicas às nossas List Comprehension
"""

# Exemplos

# 1

numeros = [1, 2, 3, 4, 5, 6]

print([numero for numero in numeros if numero % 2 == 0]) # pares
print([numero for numero in numeros if numero % 2 != 0]) # impares
 
# Refatorar

# Qualquer número par módulo 2 é 0, e 0 em Python é False, not False = True
print([numero for numero in numeros if not numero % 2 ]) # pares

# Qualquer númerp impar módulo de 2 é 1, e 1 em Python é True
print([numero for numero in numeros if numero % 2 ]) # impares 

# 2 

numeros = [1, 2, 3, 4, 5, 6]

print([n * 2 if n % 2 == 0 else n / 2 for n in numeros])