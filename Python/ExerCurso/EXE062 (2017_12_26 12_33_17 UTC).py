a1 = int(input('\033[1;35mPrimeiro Termo: '))
r = int(input('Razão da PA: '))
res = 10
rep = 0
while res != 0:
    an = a1 + (res + rep - 1) * r
    vs = a1
    while a1 <= an:
        print('\033[1;36m {}'.format(a1), end=' ')
        a1 += r
    print('\033[1;37mPAUSE')
    res = int(input('\033[1;30m Quantos Termos você quer mostrar a mais?:'))
    rep += res
    a1 = vs
print('\033[1;31m FIM')



# Resposta do Guanabara

primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão da PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{}'.format(termo), end=' ')
        termo += razão
        cont += 1
    print('pause')
    mais = int(input('Quantos Termos você quer mostrar a mais?:'))
print('FIM')