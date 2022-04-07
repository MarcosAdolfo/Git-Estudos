cor = {'amar': '\033[1;33m', 'azul': '\033[1;34m'}
aluno = dict()
aluno['nome'] = str(input(f'{cor["azul"]} Nome: '))
aluno['media'] = float(input(f'{cor["azul"]} Media: '))
if aluno['media'] >= 6:
    aluno['situacão'] = 'Aprovado'
elif aluno['media'] < 6 and aluno['media'] > 3:
    aluno['situacão'] = 'em Recunperação'
else:
    aluno['situacão'] = 'Reprovado'
print(cor["amar"], '=' * 50)
print(f'{cor["azul"]}{aluno}')
print(cor['amar'], '=' * 50)
for k, v in aluno.items():
    print(f'{cor["azul"]}{k} {v}')


print('\033[1;35m')

                                # Resposta do Guanabara
#Imgual aminha
