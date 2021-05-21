"""
Funções com Parâmetro (de entrada)

- Funções que recebem dados para serem processados dentro da mesma;
Se a gente pensar em um programa qualquer, geralmente temos:
entrada -> processamento -> saída
Se pensarmos em função, já sabemos que temos funções que:
- Não possuem entrada;
- Não possuem saída;
- Possuem entrada, mas não possuem saída;
- Não possuem entrada, mas possuem saída;
- Possuem entrada e saída;


Funções podem ter 'n' parâmetros de entrada. Ou seja, podemos receber como entrada
em uma função quantos parâmetros forem necessários. Eles são separados por vírgula.

# Exemplo

def soma(a,b):
    return a + b

def multiplicacao(num1, num2):
    return num1 * num2

def outra(num1, b, msg):
    return (num1 +b) * msg

print(soma(2, 5))
print(soma(10, 20))

print(multiplicacao(4, 5))
print(multiplicacao(2, 8))

print(outra(3, 2, 'Geek '))
print(outra(5, 4, 'Python '))

# Se a gente informar um número errado de parâmetro ou argumentos, teremos TypeError

# Nomeado parâmetros

def nome_completo(nome, sobrenome):
    return (f'Seu nome completo e {nome} {sobrenome}')

print(nome_completo('Angelina', 'Jolie'))
"""


# A diferença entre Parâmetros e Argumentos

# Parâmetros são variáveis declaradas na definição de uma função; def nome_completo (parâmetros)
# Argumentos são dados passados durante a execução de uma função; print(nome_completo(argumentos))
# A ordem dos parâmetros importa


# Argumentos nomeados (Keyword Arguments)
# Caso utilizemos nomes dos parâmetros nos argumentos para informá-los, podemos
# utilizar qualquer ordem
"""
print(nome_completo(nome='Angelina', sobrenome='Jolie'))
print(nome_completo(nome=nome, sobrenome=sobrenome))
print(nome_comleto(sobrenome='Jolie', nome='Angelina'))
"""

def soma_impares(numeros):
    total = 0
    for num in numeros:
        if num % 2 != 0:
            total = total + num
    return total

lista = [1, 2, 3, 4, 5, 6, 7]
print(soma_impares(lista))