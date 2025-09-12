'''
Escreva um programa em que o usuário digite um número e
apresente a tabuada do respectivo número
'''

# Recebendo número
numero = input('Digite um número: ')
# Converter número de string para inteiro
numero = int(numero)

for x in range(1, 11):
     print(str(x) + ' x ' + str(numero) + ' = ' + str(x * numero))

