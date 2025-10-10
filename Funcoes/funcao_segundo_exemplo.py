n1 = n2 = n3 = n4 = media = 0

def recebe_nota():
    nota_recebida = 0
    while nota_recebida <= 0 or nota_recebida > 10:
        print('Nota 1')
        print('Digite o valor entre 0 e 10')
        nota_recebida = float(input('Digite o valor da nota'))
    return nota_recebida

n1 = recebe_nota()
n2 = recebe_nota()
n3 = recebe_nota()
n4 = recebe_nota()

media = (n1 + n2 + n3 + n4) / 4
print(media)

'''
while n2 <= 0 or n2 > 10:
    print('Nota 2')
    print('Digite o valor entre 0 e 10')
    n2 = float(input('Digite o valor da nota'))

while n3 <= 0 or n3 > 10:
    print('Nota 3')
    print('Digite o valor entre 0 e 10')
    n3 = float(input('Digite o valor da nota'))

while n4 <= 0 or n4 > 10:
    print('Nota 4')
    print('Digite o valor entre 0 e 10')
    n4 = float(input('Digite o valor da nota'))
'''
