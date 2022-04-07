n1 = int(input('\033[1;35m Digite um número para fatorar: '))
for c in range(n1 - 1, 0, -1):
    n1 *= c
    print('\033[1;34m{} x {} = \033[1;33m{}'.format(c+1, c, n1))


  #Resposta do Guanabara

n = int(input('Digite um número para calcular seu Fatorial: '))
c = n
f = 1
print('Calculando {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
    print('{}'.format(f))
