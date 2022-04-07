from time import sleep
from random import randint
print('\033[1;36m{:\^40}'.format((' Pedra Papel Tesoura ')))
pc = randint(1,3)
print('''Escolha uma Das opções Abaixo Para Jogar!
1 - Pedra
2 - Papel
3 - Tesoura''')
rs = {1: 'Pedra', 2: 'Papel', 3: 'Tesoura'}
jogado = int(input('Jogue!: '))
print('PEDRA')
sleep(0.7)
print('PAPEL')
sleep(0.8)
print('TESOURA')
sleep(0.2)
if jogado == pc:
    print('Computador: {} \n Você: {}'.format(rs[pc], rs[jogado]))
    print('\033[1;33m Empate')
elif jogado == 1 and pc == 3 or jogado == 2 and pc == 1 or jogado == 3 and pc == 2:
    print('Computador: {} \n Você: {}'.format(rs[pc], rs[jogado]))
    print('\033[1;32m Você Ganhou!')
elif pc == 1 and jogado == 3 or pc == 2 and jogado == 1 or pc == 3 and jogado == 2:
    print('Computador: {} \n Você: {}'.format(rs[pc], rs[jogado]))
    print('\033[1;31m Você Perdeu!')
else:
    print('\033[1;31m Valo Invalido!')
