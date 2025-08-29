'''
Nas linhas abaixo, recebi o número de minutos
e converti para inteiro.
'''
minutos = input('Digite os minutos usados: ')
minutos = int(minutos)

if minutos < 200:
    preco = 0.20
else:
    if minutos <= 400:
        preco = 0.18
    else:
        preco = 0.15

total = preco * minutos
print(total)