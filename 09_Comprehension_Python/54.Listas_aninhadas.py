"""
Listas Aninhadas

- Algumas linguagens de programação (C/Java) possuem uma estrutura de dados chamadas array:
        - Unidimensionais (Arrays/Vetores);
        - Multidimensionais (Matrizes);

Em Python nós temos as listas

numeros = [1, 2, 3, 4, 5]
listas = [[1, 2, 3], [4, 5, 6,], [7, 8, 9]] # Matriz 3x3

print(listas)

# print(listas[1][0])

# Iterando com loops em uma lista aninhada

for i in listas:
    for j in i:
        print(j)
"""
"""
listas = [[1, 2, 3], [4, 5, 6,], [7, 8, 9]] # Matriz 3x3

# List Comprehention

[[print(valor) for valor in lista] for lista in listas]

"""


# Gerando um tabuleiro 3x3

tabuleiro = [[n for n in range(1, 4)] for valor in range (1, 4)]
print(tabuleiro)

# Gerando jogadas para o jogo da velha

velha = [['X' if n % 2 == 0 else 'O' for n in range(1,4 )] for valor in range(1,4)]

print(velha)