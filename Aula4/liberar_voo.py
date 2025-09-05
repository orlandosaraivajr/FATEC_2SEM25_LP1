print('While da NASA')
x = input("Digite um número")
# Converter o x ( tipo string) para tipo inteiro
x = int(x)

while x > 0:
    print(x)
    # x = x - 1 
    x -= 1

print('Vôo Liberado')

x = int(input("Digite outro número, menor que 100: "))

while x < 100:
    print(x)
    # x = x + 1
    x += 1

print('Cheguei no 100')
print(x)
