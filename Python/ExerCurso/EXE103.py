def ficha(nome=' ', gols=''):
    """
    -> Ficha de jogador
    :param nome: Nome do jogador
    :param gols: Gols que o jogador fez
    :return: Sem retorno
    """
    cor = ['\033[1;30m', '\033[1;31m', '\033[1;32m', '\033[1;33m', '\033[1;34m', '\033[1;35m', '\033[1;36m',
           '\033[1;37m']
    if nome == '':
        nome = '<Desconhecido>'
    if gols == '':
        gols = 0
    print(f'{cor[3]}jogador {cor[5]}{nome} {cor[3]}fez {cor[5]}{gols} {cor[3]}gol(s)')


j = str(input('\033[1;35mNome do Jogador: ')).strip().title()
g = input('\033[1;35mGols: ')
ficha(nome=j, gols=g)




print('\033[1;30m')



                                # Resposta do Guanabara


def fichas(jog='<desconhecido>', gol=0):
    print(f'O jogador {jog} fez {gol} gols(s) no campeonato.')


# Programa principal
n = str(input('Nome do jogador: '))
g = str(input('Número de Gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    fichas(gol=g)
else:
    fichas(n, g)
