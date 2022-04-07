while True:
    cont50 = cont20 = cont10 = cont1 = 0
    print('\033[1;35m{:-^40}'.format(' CAIXA ELETRÔNICO'))
    valo = int(input('Valor a ser sacado: R$'))
    while valo >= 50:
        cont50 += 1
        valo -= 50
    if cont50 >= 1:
        print(f'\033[1;33m- {cont50} notas de R$50')
    while valo >= 20:
        cont20 += 1
        valo -= 20
    if cont20 >= 1:
        print(f'\033[1;33m- {cont20} notas de R$20')
    while valo >= 10:
        cont10 += 1
        valo -= 10
    if cont10 >= 1:
        print(f'\033[1;33m- {cont10} notas de R$10')
    while valo >= 1:
        cont1 += 1
        valo -= 1
    if cont1 >= 1:
        print(f'- {cont1} notas de R$1')
    res =' '
    while res not in 'SN':
        res = str(input('\033[1;36m Deseija sai [S/N]: ')).strip().upper()[0]
    if res == 'S':
        break



                            # Resposta do Guanabara

print('=' * 30)
print('{:^30}'.format('Banco MA'))
print('=' * 30)
valor = int(input('Que valor você quer sacar? R$'))
total = valor
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cédulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break
print('=' * 30)
print('Valte sempre ao Banco MA!!! Tenha um bom dia')
