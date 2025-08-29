# numero = 360
# numero = 9
numero = int(input("Digite um número: "))

resto = numero % 2

if resto == 1:
    print(numero)
    print('Número ímpar')

if resto == 0:
    print(numero)
    print("número par")