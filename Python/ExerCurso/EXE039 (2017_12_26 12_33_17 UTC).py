from datetime import date
x = str(input('\033[1;32;47m Seu sexo é feminino ou masculino? ')).strip().lower()
if x == 'masculino':
    ano = int(input('\033[7;32m Ano de nascimento '))
    ano1 = date.today().year
    id = ano1 - ano
    if id == 18:
         print('\033[1;32m Voce Nasceu em {} tem {}Anos é ja esta na Hora de se alistar! '.format(ano, id))
    elif id > 18:
         print('\033[1;32mVoce Nasceu em {} tem {}Anos ja passou do tempo de se Alistar!'.format(ano, id))
         print('Jase Passou {}Anos do Ano do Alistamento'.format(id - 18))
         print('Voce De veria te se alistado em {}!'.format(ano1 - (id - 18)))
    else:
        print('\033[1;32m Voce Nasceu em {} tem {}Anos é ainda vai se alistar!'.format(ano, id))
        print('Falta {} para voce se alistar'.format(18 - id))
        print('Voce vai ser alista em {}!'.format(ano1 + (18 - id)))
else:
    print('\033[1;32;45m Voce é Mulher e Não precisa se Alistar!')