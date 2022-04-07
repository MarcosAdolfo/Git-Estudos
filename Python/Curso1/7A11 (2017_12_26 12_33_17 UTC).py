"""\033[0;30;41m
\033[1;37;41m
\033[7;30m"""
print('\033[1;32;mOla mundo\033[m')
print('\033[7;30;mOi bem vindo\033[m')
n = str(input('Seu nome é ?')).strip().lower()
n1 = n.split()
nome = print('Oi Tudo Bem {}{}{}{}'.format('\033[1;33m', n1[0].title(), '\033[4;32m', n1[len(n1)-1].title()))
