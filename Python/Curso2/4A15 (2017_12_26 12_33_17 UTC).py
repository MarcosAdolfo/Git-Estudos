cont = 1
while cont <= 10:
    print(cont,end=' ')
    cont += 1
print('acabal')

'''
n = s = 0
while n != 999:
    n = int(input('Digite um numero'))
    cont += 1
    s += n
print('Asoma é {}'.format(s))

'''

n = s = 0
while True:
    n = int(input('Digite um numero'))
    if n == 999:
        break
    cont += 1
    s += n
#print('Asoma é {}'.format(s))
print(f'A soma é {s} e foi digitados {cont} Numeros')

