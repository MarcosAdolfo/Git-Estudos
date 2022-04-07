var = []
pma = []
pme = []
for c in range(0, 5):
    var.append(int(input(f'\033[1;36mDigite o valor da posição {c}: ')))
ma = me = var[0]
for c in range(0, 5):
    if var[c] > ma:
        ma = var[c]
    if var[c] < me:
        me = var[c]
for p, c in enumerate(var):
    if c == ma:
        pma.append(p)
    if c == me:
        pme.append(p)
print(f'\033[1;34m O maior valor é {ma} que aparece na posição {pma}')
print(f'\033[1;33m O menor valor é {me} que aparece na posição {pme}')







print('\033[1;35m')
                                    # Resposta do Guanabara



listanum = []
mai = 0
men = 0
for c in range(0, 5):
    listanum.append(int(input(f'Digite um valor para a posição {c}: ')))
    if c == 0:
        mai = men = listanum[c]
    else:
        if listanum[c] > mai:
            mai = listanum[c]
        if listanum[c] < men:
            men = listanum[c]
print('=-' * 30)
print(f'Você digitou os valores {listanum}')
print(f'O maior valor digitado foi {mai} nas posições ', end='')
for i, v in enumerate(listanum):
    if v == mai:
        print(f'{i}... ', end='')
print()
print(f'O menor valor digitado foi {men} nas posições ', end='')
for i, v in enumerate(listanum):
    if v == men:
        print(f'{i}...', end='')
print()
