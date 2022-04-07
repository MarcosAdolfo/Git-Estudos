from datetime import date
ano = int(input('\033[1;31m Um ano para analisa.0 para a data atual '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('\033[1;34m O ano {} é Bissexto'.format(ano))
else:
    print('\033[1;31m O ano {} Não é Bissexto '.format(ano))
