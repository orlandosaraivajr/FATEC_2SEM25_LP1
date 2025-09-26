N = input('')
N = int(N)

for i in range(N):
    valor_recebido = input('')
    T, U, P = tuple(valor_recebido.split(' '))
    T = float(T)
    U = float(U)
    P = int(P)
    if P == 1:
        print('NAO REGAR')
    else:
        if T > 30 and U < 50:
            print('REGAR')
        else:
            print('NAO REGAR')