lis = list()
lispa = []
lisin = []
rsp = ' '
while rsp != 'n':
    rsp = ' '
    lis.append(int(input('\033[1;36m Digite um numero: ')))
    while rsp not in 'ns':
        rsp = str(input('Dejeija continua? Sim ou Não ')).strip().lower()[0]
for p in lis:
    if p % 2 == 0:
        lispa.append(p)
    else:
        lisin.append(p)
print(f'O valor da lista é {lis}')
print(f'Os valores pares são: {lispa}')
print(f'Os valores impas são: {lisin}')






print('\033[1;33m')

                                    # Resposta do Guanabara




num = list()
pares = list()
impares = list()
while True:
    num.append(int(input('Digite um número: ')))
    resp = str(input('Quer contunuar? [S/N] '))
    if resp in 'Nn':
        break
for i, v in enumerate(num):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)
print('-='*30)
print(f'A lista completa é {num}')
print(f'A lista de pares é {pares}')
print(f'A lista de ímpares é {impares}')
