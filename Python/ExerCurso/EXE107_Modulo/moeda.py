def metade(num):
    num /= 2
    return num


def dobro(num):
    num *= 2
    return num


def almentar(num):
    res = (num * 10) / 100
    num += res
    return num


def diminuir(num):
    res = (num * 10) / 100
    num -= res
    return num



                                # Resposta do Guanabara


def al(pre, taxa):
    res = pre + (pre * taxa / 100)
    return res


def di(pre, taxa):
    res = pre - (pre * taxa / 100)
    return res


def do(pre):
    res = pre * 2
    return res


def me(pre):
    res = pre / 2
    return res
