no = str(input('\033[1;37m Digite uma Frase ')).strip().upper()
fd = no.split()
fd = ''.join(fd)
nl = len(fd)
iv = ''
for c in range(nl, 0, -1):
    iv += fd[c - 1]
if iv == fd:
    print('\033[1;35m Temos um Palíndromo!')
else:
    print('\033[1;37m A frase digitada não é um palíndromo!')
print('Frase é {} o inverso é {}'.format(no, iv))


# 2° Modo

no = str(input('\033[1;37m Digite uma Frase ')).strip().upper()
fd = no.split()
fd = ''.join(fd)
iv = fd[::-1]
if iv == fd:
    print('\033[1;35m Temos um Palíndromo!')
else:
    print('\033[1;37m A frase digitada não é um palíndromo!')
print('Frase é {} o inverso é {}'.format(no, iv))
