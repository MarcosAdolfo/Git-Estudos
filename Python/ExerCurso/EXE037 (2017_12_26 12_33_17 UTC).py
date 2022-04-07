num = int(input('\033[1;34m Um Numero? '))
print('Bases de Conversão')
print('-1 para Binário')
print('-2 para Octal')
print('-3 Para Hexadecimal')
es = int(input('\033[1;34m Qual é a Base de Conversão? '))
if es == 1:
    print('O valo de {} em Binário é \033[1;36m {}'.format(num, bin(num)[2:]))
elif es == 2:
    print('O valor de {} em Ocatal é \033[1;36m {}'.format(num, oct(num)[2:]))
elif es == 3:
    print('O valor de {} em Hexadecimal é \033[1;36m {}'.format(num, hex(num)[2:]))
else:
    print('\033[1;31m Valor invalido!')
