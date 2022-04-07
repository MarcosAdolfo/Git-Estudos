dados = list()
aluno = []
nota = []
res = ' '
med = no = r = 0
nn = 2
while res not in 'N':
    res = ' '
    aluno.insert(0, input('\033[1;38mNome: '))
    for n in range(1, nn + 1):
        no = int(input(f'Nota {n}: '))
        med += no
        nota.append(no)
    aluno.append(med/nn)
    aluno.append(nota[:])
    dados.append(aluno[:])
    aluno.clear()
    nota.clear()
    while res not in 'SN':
        res = input('Que Continuar? [S/N]: ').strip().upper()[0]
print('-=-' * 20)
print('\033[1;33mNo. Nome                Media')
for l in range(len(dados)):
    print(l, end=' ')
    print(f'{dados[l][0]:<22}{dados[l][1]:^5.1f}')
while True:
    r = int(input('\033[1;34;Mostrar nota de qual aluno? (999 Para sai): '))
    if r == 999:
        break
    print(f'A nota de {dados[r][0]} são {dados[r][2]}')




print('\033[1;35m')



                                    # Resposta do Guanabara

ficha = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota1: '))
    nota2 = float(input('Nota2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'{"NO.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 26)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-' * 35)
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if opc == 999:
        print('FINALIZANDO...')
        break
    if opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
print('<<< VOLTE SEMPRE >>>')
