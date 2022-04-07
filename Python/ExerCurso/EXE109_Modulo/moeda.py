def metade(num):
    res = num / 2
    return res


def dobro(num):
    res = num * 2
    return res


def almentar(num, ps=0):
    res = num + (num * ps / 100)
    return res


def diminuir(num, ps=0):
    res = num - (num * ps / 100)
    return res


def moedas(va='0', fu='', moe='R$', porc=0, formata=True):
    """
    >-> Recebe um valo tanto em FLOAT ou STR-comvert para FLOAT-, e realisa outras funções caso seija requisitado, como
    Dobra ou diminuir o valor pega a metade ou almentar tantos por cento de um valor, No final retorna o valor
    formatado ou não
    :param va: Valor requerido em FLOAT ou STR-convert para FLOAT-
    :param fu: A Função que vai ser realisada no valor: 'metade', 'dobro', 'almentar' e 'diminuir'
    :param moe: A simbologia da moeda que sera mostrada na formatação. padrão 'R$'
    :param porc: A porcentajem que vai ser almentada ou diminuida na função 'almentar'
    :param formata: Se vai qure o resutado formatado ou não. O valor padrão e True
    :return: O valor formatado ou não
    """
    if ',' in va:
        va = va.replace(',', '.')
    va = float(va)
    if fu == 'metade':
        va = metade(va)
    elif fu == 'dobro':
        va = dobro(va)
    elif fu == 'almentar':
        va = almentar(va, porc)
    elif fu == 'diminuir':
        va = diminuir(va, porc)
    if formata:
        return f'{moe}{va:>.2f}'.replace('.', ',')
    else:
        return va


                                # Resposta do Guanabara


def al(pre=0, taxa=0, formato=False):
    res = pre + (pre * taxa / 100)
    return res if formato is False else moeda(res)


def di(pre=0, taxa=0, formato=False):
    res = pre - (pre * taxa / 100)
    return res if formato is False else moeda(res)


def do(pre=0, formato=False):
    res = pre * 2
    return res if not formato else moeda(res)


def me(pre=0, formato=False):
    res = pre / 2
    return res if not formato else moeda(res)


def moeda(pre=0, moeda='R$'):
    return f'{moeda}{pre:>.2f}'.replace('.', ',')
