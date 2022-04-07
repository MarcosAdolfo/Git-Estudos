a1 = int(input('\033[1;35m Primeiro termo: '))
r = int(input('\033[1;35m Razão:'))
an = a1 + (10 - 1) * r
while a1 <= an:
    print('\033[1;36m {}'.format(a1), end='')
    a1 += r
print('\033[1;37m Fim')

    # Resposta do Guanabara
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão da PA: '))
termo = primeiro
cont = 1
while cont <= 10:
    print('{}'.format(termo), end=' ')
    termo += razão
    cont += 1
print('FIM')
