cor = ['\033[1;30m', '\033[1;31m', '\033[1;32m', '\033[1;33m', '\033[1;34m', '\033[1;35m', '\033[1;36m', '\033[1;37m']
pessoas = list()
dados = {'Nome': 'VAZIO', 'Sexo': 'NÃO DE FINIDO', 'Idade': 0}
sn = ' '
mdi = 0
print(cor[4], '<>' * 30)
while sn != 'N':
    dados['Nome'] = str(input(f'{cor[6]}  Nome: ')).strip().title()
    dados['Sexo'] = str(input('  Sexo M/F :')).strip()[0].upper()
    dados['Idade'] = int(input('  Idade: '))
    mdi += dados['Idade']
    pessoas.append(dados.copy())
    sn = ' '
    while sn not in 'SN':
        sn = str(input(f'{cor[3]}Deseja cadastra mais alguém, sim ou não? [S/N]: ')).strip().upper()
        if sn == 'NÃO' or sn == 'SIM' or sn == 'NAO' or sn in 'SN':
            sn = sn[0]
        else:
            print(f'{cor[1]}{"ERRO!":^40} \n    Digite apenas Sim-[S] ou Não-[N]!')
print(cor[4], '_' * 40, '\n')
print(f'{cor[3]}          Cadastro Finalizado')
print(cor[4], '_' * 40, '\n')
print(f'{cor[6]}  >>> Pessoas Cadastradas: {len(pessoas)}')
print(f'  >>> A media das idades é: {mdi / len(pessoas):5.2f}')
print(f'  >>> As mulheres cadastradas foram:', end=' ')
for v in pessoas:
    if v['Sexo'] == 'F':
         print(v["Nome"], end=', ')
print('\n  >>>Pessoas a cima da media das idades:')
for v in pessoas:
    if v['Idade'] > mdi / len(pessoas):
        print(f'    Nome: {v["Nome"]}; Sexo: {v["Sexo"]}; Idade: {v["Idade"]}')
print(f'{cor[3]}{"<<< FIM >>>":^40} \n{cor[4]}{"<>" * 30}')



print('\033[1;38m')

                                # Resposta do Guanabara

galera = list()
pessoa = dict()
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor , digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade'))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Que continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responde apenas S ou N.')
    if resp == 'N':
        break
print('-=' * 30)
print(f'A) Ao todo temos {len(galera)} pessoas cadastradas.')
media = soma / len(galera)
print(f'B) A média de idade é de {media:5.2f} anos.')
print(f'C) As mulheres cadastradas foram ', end='')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]} ', end='')
print()
print('D) Lista das pessoas que estão acima da média: ')
for p in galera:
    if p['idade'] >= media:
        print('    ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<< ENCERRADO >>')
