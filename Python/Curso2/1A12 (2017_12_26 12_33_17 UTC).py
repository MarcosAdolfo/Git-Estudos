nome = str(input('Qual é seu nome?')).strip().lower()
if nome == 'marcos adolfo':
    print('\033[1;32m Oi chefe, como vai! ')
elif nome == 'joão' or nome == 'maria' or nome == 'pedro':
    print('\033[1;33m Seu nome é bem popular no Brasil')
elif nome in 'ana claudia gabriela julia':
    print('\033[1;35m Belo Nome Feminino')
else:
    print('oi {} \n Legal sel nome!'.format(nome.title()))
