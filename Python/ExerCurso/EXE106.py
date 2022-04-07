def titulo(txt, COR=0):
    """
    >> Função que cria Titulos
    :param txt: Texto do Titulo
    :param COR: tema do titulo de 0 a 9 temas diferentes
    :return: Não a Retorno
    """
    cor = ['\033[1;30;42m', '\033[1;31;40m', '\033[1;32;40m', '\033[1;30;44m', '\033[1;30;46m', '\033[1;30;43m', '\033[1;35;40m',
           '\033[1;30;43m', '\033[1;30;45m', '\033[1;36;40m']
    print(f'{cor[COR]}_' * (len(txt) + 10))
    print(f'\n   {txt}')
    print(f'{cor[COR]}_' * (len(txt) + 10))
    print()


def bibli():
    """
    ---> Manual de Comandos de Função e Biblioteca
    :return: help da Função ou Biblioteca que foi solicitada
    """
    from time import sleep
    while True:
        titulo('Sistema de Ajuda PyHELP', COR=0)
        f = input('\033[1;30mFunção ou Biblioteca: ').strip()
        if f == 'fim':
            titulo(f'{"Fim":^10}', COR=1)
            break
        else:
            titulo(f'Acessando o manual do comando {f}', COR=3)
            sleep(3.5)
            print('\033[1;37;40m')
            help(f)
            sleep(2)


bibli()

                                # Resposta do Guanabara
titulo(' Resposta do Guanabara', COR=8)

from time import sleep
c = ('\033m',            # 0 - sem cores
     '\033[1;30;41m',    # 1 - Vermelho
     '\033[1;30;42m',    # 2 - Verde
     '\033[1;30;43m',    # 3 - Amarelo
     '\033[1;30;44m',    # 4 - Azul
     '\033[1;30;45m',    # 5 - Roxo
     '\033[7;30m'        # 6 - Branco
     );


def ajuda(com):
    titul(f'Acessando o manual do comando \'{com}\'', 4)
    print(c[6], end='')
    help(com)
    print(c[0], end='')
    sleep(2)


def titul(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f' {msg}')
    print('~' * tam)
    print(c[0], end='')
    sleep(1)


# Programa Principal
comando = ''
while True:
    titul('SISTEMA DE AJUDA PyHELP', 2)
    comando = str(input("Função ou Biblioteca > "))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titul('Ate Logo!', 1)
