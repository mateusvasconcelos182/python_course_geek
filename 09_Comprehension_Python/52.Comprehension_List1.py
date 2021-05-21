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