r = 's'
while r == 's':
    int(input('\033[1;34mDigite um valo '))
    r = str(input('Que continua? S ou N')).strip().lower()
print('Fim')

n = 1
par = impar = 0
while n != 0:
    n = int(input('\033[1;35mDigite um numero: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1

print('\033[1;31m {} numeros Pares é {} Impas'.format(par, impar))
