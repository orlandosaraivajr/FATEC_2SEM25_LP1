'''
1. Média de notas com quantidade variável
 - Solicite ao usuário quantas notas deseja informar.
 - Leia todas as notas e calcule a média.
Informe se o aluno foi aprovado (média ≥ 7) ou reprovado.
'''

# Solicite ao usuário quantas notas deseja informar.
numero_notas = input("Digite quantas notas deseja informar")
# Convertendo o número de notas de string para inteiro
numero_notas = int(numero_notas)

soma = 0

# Leia todas as notas 
for numero in range(numero_notas):
    numero_recebido = int(input('Digite uma nota:  '))
    soma = soma + numero_recebido

# calcule a média
media = soma / numero_notas
print(media)

# Informe se o aluno foi aprovado (média ≥ 7) ou reprovado.
if media >= 7:
    print('Aprovado')
else:
    print('Reprovado')
    