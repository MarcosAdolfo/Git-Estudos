from random import randint
na = 0
md = 0
idadeh = ''
ho = 'Não a Homes'
mv = 0
cor2 = randint(30, 37)
for c in range(1, 5):
    cor = randint(30, 37)
    print('\033[1;{}m {:§^40}'.format(cor, ' Nome '))
    print('{}° PESSOA'.format(c))
    nom = str(input(' Nome ')).strip().lower()
    idade = int(input(' Idade '))
    sexo = str(input('Sexo F/M ')).strip().lower()
    md += idade
    if sexo == 'm' or sexo == 'masculino':
        na += 1
        if na == 1:
            idadeh = idade
            ho = nom
        if idadeh < idade:
            idadeh = idade
            ho = nom
    if sexo == 'f' and idade < 20 or sexo == 'feminino' and idade < 20:
            mv += 1

print('''\033[1;{}m 
A média de idade do grupo é {}
O homem mais velho é {} e tem {}
é tem {} mulheres com menos de 20 anos'''.format(cor2, md / 5, ho, idadeh, mv))
