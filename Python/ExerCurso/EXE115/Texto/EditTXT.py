def titulo(txt='Texto', decora='', cor=(3, 6, 3), am=1):
    tam = len(txt) * am
    tam1 = (tam * 2 + 12)
    tam2 = int(tam / 2)


    print(f'\033[3{cor[1]}m{decora * tam1}\033[m')
    print(f'\033[3{cor[2]}m{"-" * tam2:>{tam}}\033[m', end='')
    print(f'\033[3{cor[0]}m {txt} \033[m', end='')
    print(f'\033[3{cor[2]}m{"-" * tam2:<{tam}}\033[m')
    print(f'\033[3{cor[1]}m{decora * tam1}\033[m')


def texto(txt, cor='8', r=True):
    """

    :param txt: Texo que sera editado/printado
    :param cor: cor do texto
    :param r: se for True vai printa o Texto se for False vai retorna o Valo/Texto = txt
    :return: retorna o texto calso o r for False
    """
    if r:
        print(f'\033[3{cor}m{txt}\033[m')

    return f'\033[3{cor}m{txt}\033[m'


def menu(ops=('-'), inu='num', Cop='3', Cinu='4'):
    """
    Cria um menu onde as opições são inumeradas de acordo com inu
    ops: inu = Inumera com numeros
    ops: abc = Inumera com letras de acordo com o aufabeto
    ops: qualque outra simbolo/opição = vai inumera com esta opição ex: ser inu = # vai se #1 #2 #3 ...

    :param ops: Tupla com as opições do menu
    :param inu: O Inumerado Das Opções ex: 1-txt 2-txt 3-txt ...
    :param Cop: Cor da opição
    :param Cinu: Cor do inumerado
    """
    if inu == 'num':
        for x in range(len(ops)):
            print(texto(x+1, Cinu, False), end=' ')
            print(texto(ops[x], Cop, False))
    elif inu == 'abc':
        abc = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Z')
        for x in range(len(ops)):
            print(texto(abc[x],Cinu,False),end=' ')
            print(texto(ops[x], Cop, False))
    else:
        for x in range(len(ops)):
            print(texto(inu,Cinu,False),end=' ')
            print(texto(ops[x], Cop, False))
