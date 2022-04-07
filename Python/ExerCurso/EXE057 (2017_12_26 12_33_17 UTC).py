sexo = ''
while sexo != 'f' and sexo != 'm':
     sexo = str(input('\033[1;37m Seu Sexo F/M: ')).strip().lower()[0]
     if sexo != 'f' and sexo != 'm':
        print('\033[1;31m Sexo invalido!')
print('\033[1;34m Sexo cadastrado')

# resposta

sexo = str(input('\033[1;35m Informe seu sexo: F/M ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('\033[1;31mDados inválidos. Por favor, informe seu sexo: ')).strip().upper()[0]
print('\033[1;34mSexo {} resgistrado com sucesso '.format(sexo))
