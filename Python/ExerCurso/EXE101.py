from datetime import datetime
cor = ['\033[1;30m', '\033[1;31m', '\033[1;32m', '\033[1;33m', '\033[1;34m', '\033[1;35m', '\033[1;36m', '\033[1;37m']


def voto(ano=0):
    global idade
    idade = datetime.now().year - ano
    per = f'{cor[1]} ANO INVALIDO, DIGITE UM ANO DE NACIMENTO!'
    if idade >= 16 and idade < 18 or idade >= 60:
        per = f'{cor[5]}Opicional'
    if idade >= 18 and idade < 60:
        per = f'{cor[4]}Obrigatório'
    if idade < 16 and idade > 0:
        per = f'{cor[1]}Negado'
    if idade > 195:
        per = f'{cor[6]}Você ainda esta vivo?'
    return per


permi = voto(int(input(f'{cor[3]}Ano de nacimento: ')))
print(f'{cor[3]} Você tem {idade} Anos seu voto é {permi}')




print('\033[1;30m')

                                # Resposta do Guanabara


def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA.'
    elif 16 <= idade < 18 or idade > 65:
        return f'com {idade} anos: VOTO OPCIONAL.'
    else:
        return f'com {idade} anos: VOTO OBRIGATÓRIO.'


# Programa principal
nasc = int(input('Em que ano voê nasceu? '))
print(voto(nasc))
