cor = ['\033[1;30m', '\033[1;31m', '\033[1;32m', '\033[1;33m', '\033[1;34m', '\033[1;35m', '\033[1;36m', '\033[1;37m']
jogadores = []
jogado = dict()
gols = list()
res = ' '
while res != 'N':
    res = ' '
    jogado['Nome'] = str(input(f'{cor[6]}Nome: ')).title()
    cg = int(input(f'Quantas partidas {jogado["Nome"]} jogou? '))
    for j in range(cg):
        gols.append(int(input(f'Quantas gols na partida {j + 1}? ')))
    jogado['Gols'] = gols[:]
    gols.clear()
    jogadores.append(jogado.copy())
    while res not in 'SN':
        res = str(input(f'{cor[5]}Quer continuar? Sim-[S] ou Não-[N]: ')).strip().upper()
        if res == 'SIM' or res == 'NÃO' or res == 'NAO' or res in 'SN':
            res = res[0]
        else:
            print(f'{cor[1]}{">>> ERRO! <<<":^30} \n Digite apenas SIM-[S] ou NÃO-[N]!')
print(f'{cor[6]}-<>-' * 20)
print(f'{cor[5]} {"Cod":<4} {"Nomes":<20} {"Gols":^10} {"Total":>10} \n {"__" * 20} \n')
for c, v in enumerate(jogadores):
    print(f'{cor[6]} {c:<4} {jogadores[c]["Nome"]:<20} {jogadores[c]["Gols"]} {sum(jogadores[c]["Gols"]):>10} ')
print(f'{cor[5]} {"__" * 20}')
while True:
    res = int(input(f'{cor[5]}Mostra dados de qual jogador? (999 para Sai): '))
    if res == 999:
        break
    if res <= len(jogadores):
        print(f'{cor[6]}Levatamento do jogador {jogadores[res]["Nome"]}: ')
        for v, r in enumerate(jogadores[res]["Gols"]):
            print(f'No jogo {v + 1} fez {r} gols.')
    else:
        print(f'{cor[1]}Jogador Não esiste!')
print(f'{cor[6]}-<>-' * 20)
print(jogadores)





print('\033[1;38m')



                                                # Resposta do Guanabara



time = list()
jogador = {}
partidas = list()
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do Jogador: '))
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f'    Qantos gols na partida {c}?')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('Que continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break
print('-=' * 30)
print('Cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-=' * 30)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 30)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar'))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe Joggador com código {busca}!')
    else:
        print(f' -- Levantamento do Jogador com código {busca}!')
        for i, g in enumerate(time[busca]['gols']):
            print(f'   No jogo {i + 1} fez {g} gols.')
    print('-' * 40)
print('<< Volte sempre >>')
