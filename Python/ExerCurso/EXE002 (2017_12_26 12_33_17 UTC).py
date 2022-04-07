nome = str(input('\033[34m Qual é Seu nome\033[m \033[31m?')).strip().lower().title()

corz = {'fim' : '\033[m',
        'azc' : '\033[36m',
        'az' : '\033[34m',
        'ver' : '\033[31m'}

print('{}Oi, Tudo bem {}{}{}{}!{} {}Seija Bem vindo{}!{}'.format(corz['azc'], corz['az'], nome, corz['fim'], corz['ver'], corz['fim'], corz['azc'], corz['ver'], corz['fim']))
