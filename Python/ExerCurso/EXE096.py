cor = ['\033[1;30m', '\033[1;31m', '\033[1;32m', '\033[1;33m', '\033[1;34m', '\033[1;35m', '\033[1;36m', '\033[1;37m']
def cabeçalho(txt):
    print(f'{cor[4]} {"_" * (len(txt) + 10)}')
    print(f'\n {cor[3]} {txt}')
    print(f'{cor[4]} {"_" * (len(txt) + 10)} \n')


def Area(lar, com):
    print(f'{cor[3]} A Largura é: {cor[4]}{lar} \n {cor[3]}O Comprimento é: {cor[4]}{com} \n {cor[3]}A Área é: {cor[4]}{lar * com}')


cabeçalho(f'{"Calcula Área":^57}')
Area(lar=float(input(f'{cor[3]} Largura: ')), com=float(input(f'{cor[3]} Comprimento: ')))
cabeçalho(f'{">>> Fim <<<":^57}')


print('\033[1;35m')

                                # Resposta do Guanabara

def área(larg, comp):
    a = larg * comp
    print(f'A área de um terreno {larg}x{comp} é de {a}m².')


# Programa principal
print(' Controle de Terrenos')
print('-' * 20)
l = float(input('Largura (m): '))
c = float(input('Comprimento (m): '))
área(l, c)
