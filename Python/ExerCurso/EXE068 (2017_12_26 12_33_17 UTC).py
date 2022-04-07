from random import randint
print('\033[1;33m {:=^30}'.format(' Par ou Ímpar '))
cont = 0
while True:

    pc = randint(0, 10)
    es = input('\033[1;34mPar ou Ímpar [p/i]? X Para SAIR ').strip().lower()[0]
    if es == 'x':
        break
    jo = int(input('Seu numero de 0 a 10: '))
    pi = pc + jo
    g = pi % 2
    print(f'Você jogo {jo} e o Computador {pc} que da {pi}')
    if g == 0 and es == 'p' or g == 1 and es == 'i':
        cont += 1
        print('\033[1;32m Você ganhou!')
    else:
        print('\033[1;32mPC ganhou!')
        print('\033[1;31mVocê perdeu! ')

print(f'\033[1;32mvocê teve {cont} Vitorias ')




        # Resposta do Guanabara


from random import randint
v = 0
while True:
    jog = int(input('\033[1;34mDiga um valor: '))
    com = randint(0, 10)
    total = jog + com
    tipo = ''
    while tipo not in 'PI':
        tipo = str(input('Par ou Impar? [P/I] ')).strip().upper()[0]
    print(f'Você jogou {jog} e o computador {com}. Total de {total} ',end='')
    print('DEU PAR' if total % 2 == 0 else ' DEU IMPAR ')
    if tipo == 'P':
        if total % 2 == 0:
            print('você venceu!')
            v += 1
        else:
            print('você perdeu!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('você venceu!')
            v += 1
        else:
            print('você perdeu!')
            break
    print('vamos jogar novamente...')
    print(f'GAME OVER! Você venceu {v} vezes.')
