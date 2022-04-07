from random import randint
from time import sleep
jogadores = {}
mm = []
me = mar = 'Jogado 1'
for c in range(4):
    jogadores[f'Jogado {c+1}'] = randint(1, 6)
for cc in range(4):
    if cc > 0:
        mm.insert(0, mar)
    mar = me
    for j, r in jogadores.items():
        if r > jogadores[mar] and cc == 0:
            mar = j
        if r < jogadores[me]:
            me = j
        elif r >= jogadores[mar] and j not in mm and cc > 0:
            mar = j
    if mar not in mm or cc == 0:
        print(f'\033[1;34m{mar}: \033[1;35m{jogadores[mar]}')
        sleep(1)



print('\033[1;35m')


                                # Resposta do Guanabara


from random import randint
from time import sleep
from operator import itemgetter
jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6)}
ranking = list()
print('Valores sorteados:')
for k, v in jogo.items():
    print(f'{k} tirou {v} no Dado.')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('-=' * 30)
print('  == RANKING DOS JOGADORES ==  ')
for i, v in enumerate(ranking):
    print(f'  {i + 1}° lugar: {v[0]} com {v[1]}.')
    sleep(1)
