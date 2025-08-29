# numero = 200

# Na linha abaixo, recebo o número digitado
numero = input("Digite um número inteiro: ")
# Na linha abaixo, converto a variável numero
# de string (str) para inteiro (int)
numero = int(numero)

if numero % 2 == 1:
    print('Número ímpar')
    print(numero)
    print('passei por aqui')

if numero % 2 == 0:
    print('Número par')
    print(numero)
    print('Passei por aqui 2')

print('acabou o programa')    