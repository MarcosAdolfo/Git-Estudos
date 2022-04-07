idadeM = totalID = totalff = totalm = 0
while True:
    print('\033[1;35m {:=^30}'.format('Cadastro'))
    nome = str(input('\033[1;36m Digite o Nome Completo: ')).upper()
    idade = int(input('\033[1;36m Digite a Idade: '))
    sexo = str(input('\033[1;36m SEXO Masculino ou Feminino [M/F]')).strip().lower()[0]
    if idade > 18:
        totalID += 1
    if idade > idadeM:
        idadeM = idade
        nomeM = nome
    if idade < 20 and sexo == 'f':
        totalff += 1
    if sexo == 'm':
        totalm += 1
    fim = input('\033[1;34m Dejeija Finalisa [S/N]: ').strip().lower()[0]
    if fim == 's':
        break
print(f'\033[1;33m Tem {totalID} pessoas maiores de idade, {totalff} '
      f'mulheres com menos de 20 anos, {totalm} Homes cadastrados e {nomeM} é a pessoa mais velha com {idadeM} anos')







                                 # Resposta do Guanabara

tot18 = totH = totM = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        totH += 1
    if sexo == 'F' and idade < 20:
        totM += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {tot18} '
      f'Ao todo temos {totH} homes cadastrados e temos {totM} mulheres com menos de 20 anos')
