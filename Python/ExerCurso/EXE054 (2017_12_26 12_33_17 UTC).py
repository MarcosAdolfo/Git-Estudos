from datetime import date
datan = date.today().year
maio = 0
meno = 0
for c in range(1, 7+1):
    data = int(input('\033[1;35m{}° Data de nascimento'.format(c)))
    ida = datan - data
    if ida >= 18:
        maio += 1
    else:
        meno += 1
print('\033[1;36m {} são de maiores é {} de menores '.format(maio, meno))