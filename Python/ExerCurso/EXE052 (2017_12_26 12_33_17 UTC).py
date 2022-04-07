nu = int(input('\033[1;34m Digite um Número: '))
to = 0
for c in range(1, nu + 1):
    if nu % c == 0 and nu / nu == 1:
        print('\033[1;31m', end=' ')
        to += 1
    else:
        print('\033[1;33m', end=' ')
    print('{}'.format(c), end=' ')
print('\n\033[1;34mO número {} foi divisível {} Veses'.format(nu, to))
if to == 2:
    print('E por isso ele é Primo!')
else:
    print('E por isso ele Não é Primo!')
