from datetime import datetime
trabalhado = dict()
trabalhado['nome'] = str(input('\033[1;35mNome: '))
trabalhado['nacimento'] = int(input('Ano de Nacimento: '))
trabalhado['idade'] = datetime.now().year - trabalhado['nacimento']
trabalhado['carteira de trabalho'] = int(input('Carteira de Trabalho (0 Não Tem): '))
if trabalhado['carteira de trabalho'] != 0:
    trabalhado['contratação'] = int(input('Ano de contratação: '))
    trabalhado['salario'] = int(input('Salario: '))
    trabalhado['aposentadoria'] = trabalhado['contratação'] - trabalhado['nacimento'] + 35
print('=' * 30)
for k, v in trabalhado.items():
    print(f'\033[1;33m{k} Tem o Valhor \033[1;35m{v}')



print('\033[1;34m')


                                # Resposta do Guanabara
from datetime import datetime
dados = dict()
dados['nome'] = str(input('Nome: '))
nasc = int(input('Ano de Nasimento: '))
dados['idade'] = datetime.now().year - nasc
dados['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if dados['ctps'] != 0:
    dados['contraração'] = int(input('Ano de Contratação: '))
    dados['salario'] = float(input('Salario: R$'))
    dados['aposentadoria'] = dados['idade'] + ((dados['contraração'] + 35) - datetime.now().year)
print('-=' * 30)
for k, v in dados.items():
    print(f'- {k} tem o valor {v}')
