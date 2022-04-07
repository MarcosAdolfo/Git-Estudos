from ExerCurso.EXE115.Texto import EditTXT


def Verificado(msg=': ', compara=()):
    """
    O verificado vai Faze uma pegunta e compara para ver ser é verdadeira ou falsa.
    a pergunta e defenida em (msg) eos criterios de comparação em (compara)

    :param msg: Mensagem que sera perguntada, Caso nada seja colocado Automaticamente sera definido dois ponto( : )
    :param compara: com oque a resposta sera comparado
    :return: retonara verdadeiro ou falso quando conpara a resposta com o requisitos(compara)
    """
    try:
        opicao = str(input(msg)).strip().lower()
    except KeyboardInterrupt:
        print('O Usuario Preferio não digita nada!')
    except:
        print('\033[31m ERRO!\033[m')
    else:
        if opicao in compara:
            resu = (True, opicao)
            return resu
        else:
            return False


def quest(*msg):
    re = {}
    for x in msg:
        print(EditTXT.texto(x, '4', False), end='')
        rs = input(':')
        re.update({x: rs})
    return re
