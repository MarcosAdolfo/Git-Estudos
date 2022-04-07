from datetime import date
from time import sleep
ano = int(input('\033[1;35m Seu Ano de nacimento: '))
dt = date.today().year
id = dt - ano
print('Sua Categoria é')
print('...')
sleep(1)
if id <= 9:
    print('\033[1;36m MIRIM')
elif id <= 14:
    print('\033[1;36m INFANTIL')
elif id <= 19:
    print('\033[1;36m JUNIOR')
elif id <= 25:
    print('\033[1;36m SÊNIOR')
else:
    print('\033[1;36m MASTER')
