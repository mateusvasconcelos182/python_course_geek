"""
Entendendo o *args

- O *args é um parametro como outro qualquer. Isso significa que podemos chamar de qualquer coisa
desde que comece com *(asterisco).


O parâmetro *args utilizado em uma função, coloca os valores extras informados como
entrada em uma tupla. Então desde já lembre-se que tuplas são imutáveis.

def soma_todos_numeros(num1, num2, num3):
    return num1 + num2 + num3

print(soma_todos_numeros(2, 2, 2))

# Entendendo o args

def soma_todos_numeros(*args):
    return sum(args)

print(soma_todos_numeros())
print(soma_todos_numeros(1))
print(soma_todos_numeros(2, 3))
print(soma_todos_numeros(2, 3, 4))

"""


def soma_todos_numeros(*args):
    return sum(args)

numeros = [1, 2, 3, 4, 5, 6, 7]

#Desempacotar

print(soma_todos_numeros(*numeros))

# OBS: O asteristico serve para que informemos ao Python que estamos
# passando como argumento uma coleção de dados. Desta forma, ele saberá
# que precisará antes desempacotar estes dados.