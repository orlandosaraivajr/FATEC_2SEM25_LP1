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
controle = 0
# Leia todas as notas 
while controle < numero_notas:
    numero_recebido = int(input("Digite um número: "))
    soma = soma + numero_recebido
    controle = controle + 1

# calcule a média
media = soma / numero_notas
print(media)

# Informe se o aluno foi aprovado (média ≥ 7) ou reprovado.
if media >= 7:
    print('Aprovado')
else:
    print('Reprovado')
    