"""
# Funções com parâmetros padrão (Default Parameters)

- Funções onde a passagem de parâmetro seja opcional

"""

total = 0

def incrementa():
    global total
    total += 1
    return total

print(incrementa())
print(incrementa())

def fora():
    contador = 0

    def dentro():
        nonlocal contador

        contador += 1
        return contador
    return dentro()

print(fora())
print(fora())
print(fora())