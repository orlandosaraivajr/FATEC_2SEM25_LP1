n1 = n2 = n3 = n4 = media = 0

def recebe_nota(tipo_de_nota):
    nota_recebida = 0
    while nota_recebida <= 0 or nota_recebida > 10:
        print(tipo_de_nota)
        print('Digite o valor entre 0 e 10')
        nota_recebida = float(input('Digite o valor da nota'))
    return nota_recebida

n1 = recebe_nota('Nota 1')
n2 = recebe_nota('Nota 2')
n3 = recebe_nota('Nota 3')
n4 = recebe_nota('Nota 4')

media = (n1 + n2 + n3 + n4) / 4
print(media)
