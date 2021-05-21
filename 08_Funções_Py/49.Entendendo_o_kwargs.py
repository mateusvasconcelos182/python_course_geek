"""
**kwargs

Este é só mais um parâmetro, mas diferente do *args que coloca os valores extras em uma tupla,
o **kwargs exige que utilizemos parâmetros nomeados, e transforma esses parâmetros extras 
e um dicionário.


"""


def cumprimento_especial(**kwargs):
    if 'geek' in kwargs and kwargs['geek'] == 'Python':
        return 'Voce recebeu um cumprimento Pythonico Geek!'
    elif 'geek' in kwargs:
        return (f"{kwargs['geek']} Geek!")
    return 'Nao tenho certeza quem voce e ...' 

print(cumprimento_especial())
print(cumprimento_especial(geek = 'Python'))
print(cumprimento_especial(geek = 'Oi'))
print(cumprimento_especial(geek = 'Especial'))


"""
Nas nossas funções, podemos ter (NESTA ORDEM):

- Parâmetros obrigatórios;
- *args;
- Parâmetros Default (não obrigatórios);
- **kwargs

"""

def minha_funcao(idade, nome, *args, solteiro = False, **kwargs):
    print(f'{nome} tem {idade} anos')
    print(args)
    if solteiro:
        print('Solteiro')
    else:
        print('Casado')
    print(kwargs)


minha_funcao(8, 'Julia')
minha_funcao(18, 'Felicity', 4, 5, 3, solteiro=True)
minha_funcao(34, 'Felipe', eu= 'Nao', voce='Vai')
minha_funcao(19, 'Carla', 9, 4, 3, java=False, python=True)


# Desempacotando com **kwargs

def mostra_nomes(**kwargs):
    return (f"{kwargs['nome']}, {kwargs['sobrenome']}")

nomes = {'nome': 'Felicity', 'sobrenome' : 'Jones'}

print(mostra_nomes(**nomes))

#--------------------

def soma_multiplo_numeros(a, b, c):
    print(a+b+c)

lista = [1, 2, 3]
tupla = (1, 2, 3)
conjunto = {1, 2, 3}

soma_multiplo_numeros(*lista)
soma_multiplo_numeros(*tupla)
soma_multiplo_numeros(*conjunto)


dicionario = dict(a=1, b=2, c=3)

soma_multiplo_numeros(**dicionario)


