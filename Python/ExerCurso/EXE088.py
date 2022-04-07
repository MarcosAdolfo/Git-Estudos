from random import randint
from time import sleep
jogos = list()
print('\033[1;34m-' * 50)
print('\033[1;33m{:^50}'.format('JOGA NA MEGA SENA'))
print('\033[1;34m-' * 50)
nj = int(input('\033[1;33mQuantos jogos você quer que eu sorteie? '))
print('\033[1;34m-=-' * 3, f'\033[1;33mSorteando {nj} jogos', '\033[1;34m-=-' * 3)
for j in range(nj):
    for g in range(6):
        jj = randint(0, 60)
        if jj in jogos:
            jj = randint(0, 60)
        jogos.append(jj)
    print(f'\033[1;33mJogo {j + 1}: {jogos}')
    jogos.clear()
    sleep(1)
print('\033[1;34m-=-' * 3, '\033[1;33m< Boa Sorte! >', '\033[1;34m-=-' * 3)






print('\033[1;35m')




                                    # Resposta do Guanabara
from random import randint
from time import sleep
lista = list()
jogo = list()
print('-' * 30)
print('       JOGA NA MEGA SENA      ')
print('-' * 30)
quant = int(input('Quantos jogos você quer que eu sorteie? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('-=' * 3, f'SORTEANDO {quant} JOGOS ', '-=' * 3)
for i, l in enumerate(jogos):
    print(f'jogo {i+1}: {l}')
    sleep(1)
print('-=' * 5, '< BOA SORTE! >', '-=' * 5)
