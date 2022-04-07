def fatorial(num=0, show=False):
        n = num
        print(f'\033[1;33m{num}! ', end='')
        if show == True:
            for f in range(num - 1, 0, -1):
                n *= f
                print(f'x {f}', end=' ')
            print(f' = {n}')
        else:
            for f in range(num - 1, 0, -1):
                n *= f
            print(n)


fatorial(num=5, show=True)





print('\033[1;30m')




                                # Resposta do Guanabara



def fatorial(n, show=False):
    """
    -> Calcula o Fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (Opcional) Mostrar ou não a conta.
    :return: O valor do Fatorial de um número n
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


print(fatorial(5, show=True))
