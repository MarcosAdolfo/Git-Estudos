pessoas = list()
dados = []
res = ' '
while res != 'N':
    res = ' '
    dados.append(str(input('\033[1;35mNome:')))
    dados.append(int(input('Peso:')))
    pessoas.append(dados[:])
    dados.clear()
    while res not in 'SN':
        res = input('\033[1;33mQue continua Sim ou Não [S/N]? ').strip().upper()[0]
print('\033[1;35m-=-'*20)
print(f'\033[1;33mForam cadastradas {len(pessoas)} pessoas')
m = n = pessoas[0][1]
for mp in range(len(pessoas)):
    if pessoas[mp][1] > m:
        m = pessoas[mp][1]
    if pessoas[mp][1] < n:
        n = pessoas[mp][1]
print('Os mais pesados são:', end=' ')
for mp in range(len(pessoas)):
    if pessoas[mp][1] == m:
        print(pessoas[mp][0], end=', ')
print('Com ', m, 'Kg')
print('Os mais leves são:', end=' ')
for mp in range(len(pessoas)):
    if pessoas[mp][1] == n:
        print(pessoas[mp][0], end=', ')
print('Com ', n, 'Kg')





print('\033[1;35m')


                                                    # Resposta do Guanabara


temp = []
princ = []
mai = men = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(princ) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    princ.append(temp[:])
    temp.clear()
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print('-=-' * 30)
print(f'Ao todo, você cadastrou {len(princ)} pessoas.')
print(f'O maior peso foi de {mai}Kg. Pesode ', end='')
for p in princ:
    if p[1] == mai:
        print(f'[{p[0]}', end='')
print()
print(f'Omenor peso foi de {men}Kg. Peso de ', end='')
for p in princ:
    if p[1] == men:
        print(f'[{p[0]}] ', end='')
print()
