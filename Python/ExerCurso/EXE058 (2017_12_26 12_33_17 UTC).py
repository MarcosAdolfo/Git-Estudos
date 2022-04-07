from random import randint
jogado = ''
ten = 0
pc = randint(0, 10)
inicio = str(input('\033[1;33m Bora jogar um jogo! S/N ')).strip().lower()[0]
if inicio == 's':
    print('{:/^40}'.format('\033[1;34m Jogo \033[1;33m'))
    print('O jogo e bem simples, voce vai tentar adivinhar um número que eu esto pensando de 0 a 10 em menos tentativas possivas')
    print('Bora começar!')
    while jogado != pc:
        jogado = int(input('O numero que eu esto pense de 0 a 10 e?: '))
        ten += 1
        if jogado < pc:
            print('Maior que {}'.format(jogado))
        if jogado > pc:
            print('Menor que {}'.format(jogado))
    if ten == 1:
        print('\033[1;32m Voce e muito esperto Acerto de primeira!')
    if ten > 6:
        print('\033[1;31mVoce e bem burro preciso disso tudo para acertar!')
    if ten > 1 and ten <= 6:
        print('\033[1;35m Voce foi razoável!')
    print('\033[1;36m Voce preciso de {} tentativas para adivinhar que o numero que eu estava pensando era {}'.format(ten, pc))
else:
    print('\033[1;37m Esta certo !')
