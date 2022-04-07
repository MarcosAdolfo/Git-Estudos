import random

nal = random.randint(1, 5)
print('\033[1;32;40m Eu Vol pensar em um numero de 1 a 5 tente adivinha')
pes = int(input('\033[1;32;47m Qual Numero eu to pensando?'))
if pes == nal:
    print('\033[1;32m certo! eu stava pensando no {} mesmo.'.format(nal))
else:
    print('\033[1;31m Errol! eu estava pensando no {}'.format(nal))
