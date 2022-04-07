total = totmil = mbar = 0
pr = ''
while True:
    print('\033[1;36m-='*20)
    pro = str(input('\033[1;34m Nome do produto: '))
    pre = float(input('Preço do produto R$: '))
    total += pre
    if pre > 1000:
        totmil += 1
    if pre < mbar or mbar == 0:
        mbar = pre
        pr = pro
    ver = ' '
    while ver not in 'sn':
        print('\033[1;36m -' * 20)
        ver = str(input('\033[1;33m Dejeija comtinuar [S/N]: ')).strip().lower()[0]
    if ver == 'n':
        break
print('\033[1;36m-=' * 40)
print(f'\033[1;36m O total gasto é R${total}, {totmil} produtos custaram mais de R$1000 e o produto mais barato é {pr} que custa R${mbar}')
print('\033[1;36m-=' * 40)






                                   # Resposta do Guanabara

total = totmil = menor = cont = 0
barato = ''
while True:
    produto = str(input('Nome do Produto: '))
    preco = float(input('Preço: R$'))
    cont += 1
    total += preco
    if preco > 1000:
        totmil += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('{:-^40}'.format('FIM DO PROGRAMA '))
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {totmil} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {barato} que custa R${menor:.2f}')
