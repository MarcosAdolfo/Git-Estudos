num = []
conf = 's'
while conf not in 'Nn':
    n = int(input('\033[1;36m Digite um numero: '))
    while n in num:
        print(f'\033[1;31m O numero {n} já existe!')
        n = int(input('\033[1;36m Digite outro numero: '))
    num.append(n)
    num.sort()
    conf = input('\033[1;33m Deseija comtinuar sim ou não S/N : ').strip()[0]
print(f'\033[1;34m {num}')




print('\033[1;35m')
                                    # Resposta do Guanabara



numero = list()
while True:
    n = int(input('Digite um valor:' ))
    if n not in numero:
        numero.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    r = str(input('Quer continuar? [S/N] '))
    if r in 'Nn':
        break
numero.sort()
print(f'Voce digitor os valores {numero}')
