from time import sleep
from ExerCurso.EXE115.Texto import EditTXT


def salvar(dados=(), arq='Cadastro.txt'):
    """
    Vai salva tudo em uma linha no arquivo de txt definido = arq.
    sempre que for salva vai salva em uma linha nova.

    :param dados: Os dados que sera salvos
    :param arq: arquivo onde sera salvo
    :return: retorna falso se tiver algun dado vazio = ''
    """

    txt = open(arq, 'a')

    if '' in dados:
        txt.close()
        return False

    for x in range(len(dados)):
        d = str(dados[x]).strip().upper().replace(' ', '-')
        txt.write(f'{d} ')
    txt.write('\n')
    txt.close()
    return True


def ler(arq='Cadastro.txt', escreve=True):
    """

    :param arq: Arquivo que sera lido em .txt
    :param escreve: ser for True ira printa todas as linha em forma de um lista inumerada, ser for False vai retorna uma lista com todas as linhas do arquivo
    :return: ser escreve for imgual a False vai retorna uma lista contendo as linha do arquivo
    """

    while True:
        try:
            txt = open(arq, 'r')
        except:
            EditTXT.texto('Criando arquivo...', 4)
            sleep(0.5)
            salvar(('', ''), arq)
        else:
            break

    a = txt.readlines()
    txt.close()
    if escreve:
        linha = []
        for x in a:
            li = x.replace('\n', '')
            linha.append(li)
        EditTXT.menu(linha)
    else:
        return a
