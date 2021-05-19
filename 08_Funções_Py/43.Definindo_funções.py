"""
Definindo Funções

Ex: print(), len(), min(), max(), count;
- Funções são pequenos trechos de código que realizam tarefas específicas;
- Pode ou não receber entradas de dados e retornar uma saída de dados;
- Muito uteis para executar procedimentos similares repetidas vezes;

OBS: Se você escrever uma função que realiza várias tarefas dentro dela,
é bom fazer uma verificação para que a função seja simplificada;

Em Python a forma geral de definir uma função é 

def nome_da_funcao(parametros_de_entrada):
    bloco_da_funcao

Onde: 

nome_da_funcao -> sempre com letras minusculas, e se for compostos, separado por underline (Snake Case)
parametros_de_entrada -> são opcionais, onde tendo mais de um, cada um separado por virgula, podendo ser opcionais ou não
bloco_da_funcao -> também chamado de corpo da funcao ou implementacao, é onde o processamento da funcao acontece.
Neste bloco, pode ter retorno ou não da função.

OBS: Veja que para definir uma função, utilizamos a palavra reservada 'def', informando ao Python que estamos definindo
uma função, também abrimos o código de código com dois pontos ':' que é utilizado em Python para definir blocos
"""
# Como definir funções?

# Definindo a primeira função

def diz_oi():
    print('oi')

diz_oi()





