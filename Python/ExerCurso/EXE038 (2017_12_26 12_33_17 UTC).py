n1 = int(input('\033[1;30m Digite um Numero '))
n2 = int(input('Digite outro Numero'))
if n1 > n2:
    print('\033[1;33;47m O numero \033[7;37m{}\033[1;33;47m é maior que \033[7;37m {}'.format(n1, n2))
elif n1 == n2:
    print('\033[1;33m O numero {} é ingual a {}'.format(n1, n2))
else:
    print('\033[1;33;47m O numero \033[7;37m{}\033[1;33;47m é maiop que \033[7;37m {}'.format(n2, n1))
