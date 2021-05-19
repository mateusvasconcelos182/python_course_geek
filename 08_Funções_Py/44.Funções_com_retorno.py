"""
Funções com retorno

OBS: Quando uma função não retorna nenhum valor, o retorno é None
OBS: Funções Python que retornam valores, devem retornar estes valores, com a palavra reservada return
OBS: Não precisamos necessariamente criar uma variável para receber o return de uma função, podemos
passar a execução da função para outras funções.

# Exemplo função
def quadrado_de_7():
    return 7*7

print(quadrado_de_7())

OBS: Sobre a palavra return
    1 - Ela finaliza a função, ou seja, ela sai da execução da função;
    2 - Podemos ter em uma função, diferentes returns;
    3 - Podemos em uma função retornar qualquer tipo de dado e até mesmo multiplos valores;

# Exemplo 1

def diz_oi():
    return 'Oi! '
    print('Estou sendo executado após o return...') #Não executa nada após return.

print(diz_oi)

# Exemplo 2

def nova_funcao():
    variavel = None
    if variavel:
        return 4
    elif variavel is None:
        return 3.2
    return 'b'

print(nova_funcao())

# Exemplo 3

def outra_funcao():
    return 2, 3, 4, 5


print(outra_funcao())

"""

from random import random

def joga_moeda():
    valor = random()
    if valor > 0.5:
        return 'Cara'
    else:
        return 'Coroa'

print(joga_moeda())


# Erros comuns na utilização do retorno, que na verdade nem é erro, mas sim codificação desnecessária.

def eh_impar():
    numero = 5
    if numero % 2 != 0:
        return True
    return False #Sem a necessidade do else, linha desnecessária a mais

print(eh_impar())




