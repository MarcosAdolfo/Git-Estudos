from time import sleep
from random import randint


def sorteia(lst):
    print(f'\033[1;34mSorteando 5 numeros para a lista:', end=' ', flush=True)
    for c in range(5):
        sleep(0.5)
        numeros.append(randint(0, 10))
        print(f'\033[1;33m{numeros[c]}', end=' ', flush=True)


def soma(num):
    pa = 0
    for c in num:
        if c % 2 == 0:
            pa += c
    sleep(2)
    print(f'\n\033[1;34mSomando os valores pares da lista:... \n O Resutado da soma é: ', end='', flush=True)
    sleep(1)
    print(f'\033[1;33m{pa}', flush=True)


numeros = []
sorteia(numeros)
soma(numeros)






print('\033[1;35m')




                                # Resposta do Guanabara


from random import randint
from time import sleep


def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end='')
    for cont in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n} ', end='', flush=True)
        sleep(0.3)
    print('PRONTO!')


def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores pares de {lista}, temos {soma}')


numeros = list()
sorteia(numeros)
somaPar(numeros)
