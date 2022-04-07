
nm = str(input('\033[1;37;43m Seu nome')).strip().lower()
print('\033[1;33;47m Seu nome maiusculo {} '.format(nm.upper()))
print('\033[1;33;47m Seu nome minusculo {} '.format(nm))
nm1 = nm.split()
nm2 = ''.join(nm1)
print('\033[1;33;47m Seu Nome tem {} letras '.format( len(nm2)))
print('\033[1;33;47m Seu Primeiro nome {} tem {} letras'.format(nm1[0], len(nm1[0])))

