cor = {'amar': '\033[1;33m', 'azul': '\033[1;34m', 'roxo': '\033[1;35m'}
jogado = dict()
gols = []
t = 0
jogado['nome'] = str(input(f'{cor["roxo"]}Nome do Jogador: '))
partidas = int(input(f'Quantas Partidas {jogado["nome"]} Jogou: '))
for c in range(partidas):
    g = int(input(f'Quantos Gols na partida {c + 1}? '))
    gols.append(g)
    t += g
jogado['gols'] = gols
jogado['total'] = t
print(f'{cor["azul"]}-=-' * 30)
print(f'{cor["amar"]}{jogado}')
print(f'{cor["azul"]}-=-' * 30)
for k, v in jogado.items():
    print(f'{cor["azul"]}{k} é imgual a {cor["amar"]}{v}')
print(f'{cor["azul"]}-=-' * 30)
print(f'{cor["azul"]}O jogador {cor["amar"]}{jogado["nome"]} {cor["azul"]}jogou {cor["amar"]}{partidas} {cor["azul"]}partidas')
for c in range(partidas):
    print(f'{cor["amar"]}=> {cor["azul"]}Na partida {cor["amar"]}{c + 1} {cor["azul"]}Fez {cor["amar"]}{gols[c]} {cor["azul"]}gols')




print('\033[1;38m')


                                # Resposta do Guanabara

jogador = {}
partidas = list()
jogador['nome'] = str(input('Nome do Jogador: '))
tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for c in range(0, tot):
    partidas.append(int(input(f'    Qantos gols na partida {c}?')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print('-=' * 30)
print(jogador)
print('-=' * 30)
for k, v in jogador.items():
    print(f'o campo {k} tem o valor {v}')
print('-=' * 30)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
for i, v in enumerate(jogador['gols']):
    print(f'    => Na partida {i}, fez {v} gols.')
print(f'Foi um total de {jogador["total"]} gols.')
