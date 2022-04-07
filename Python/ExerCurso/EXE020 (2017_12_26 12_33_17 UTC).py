from random import shuffle
nma = str(input('\033[1;32;40m Primeiro Nome'))
nmb = str(input('\033[1;32;40m Segundo Nome'))
nmc = str(input('\033[1;32;40m Terceiro Nome'))
nmd = str(input('\033[1;32;40m Quarto Nome'))
nme = str(input('\033[1;32;40m Quinto Nome'))
lista = [nma, nmb, nmc, nmd, nme]
shuffle(lista)
print('\033[1;32;47m A lista é {}'.format(lista))
