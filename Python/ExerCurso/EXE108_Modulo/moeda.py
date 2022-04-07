def metade(num):
    if ',' in num:
        num = num.replace(',', '.')
    num = float(num)
    res = num / 2
    res = f'{res:0.2f}'
    res = str(res)
    res = res.replace('.', ',')
    return f'R${res}'



def dobro(num):
    if ',' in num:
        num = num.replace(',', '.')
    num = float(num)
    res = num * 2
    res = f'{res:0.2f}'
    res = str(res)
    res = res.replace('.', ',')
    return f'R${res}'


def almentar(num, ps=0):
    if ',' in num:
        num = num.replace(',', '.')
    num = float(num)
    res = (num * ps) / 100
    res += num
    res = f'{res:0.2f}'
    res = str(res)
    res = res.replace('.', ',')
    return f'R${res}'


def diminuir(num, ps=0):
    if ',' in num:
        num = num.replace(',', '.')
    num = float(num)
    res = (num * ps) / 100
    res -= num
    res = f'{res:0.2f}'
    res = str(res)
    res = res.replace('.', ',')
    return f'R${res}'



                                # Resposta do Guanabara


def al(pre=0, taxa = 0):
    res = pre + (pre * taxa / 100)
    return res


def di(pre=0, taxa = 0):
    res = pre - (pre * taxa / 100)
    return res


def do(pre=0):
    res = pre * 2
    return res


def me(pre=0):
    res = pre / 2
    return res


def moeda(pre=0, moeda = 'R$'):
    return f'{moeda}{pre:>.2f}'.replace('.', ',')