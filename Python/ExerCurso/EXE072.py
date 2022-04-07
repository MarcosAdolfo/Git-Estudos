numero = ('Zero', 'Um', 'Dois', 'Treiz', 'Quatro', 'Cinco', 'Seis',
          'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze',
          'Catoze', 'Quinze', 'Dizesseis', 'Dizessete', 'Dezoito', 'Dizenove', 'Vinte')
ln = (0, 1, 2 , 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)
nn = ' '
while nn not in ln:
    nn = int(input('\033[1;35m Digite um Numero entre 0 e 20: '))
print('\033[1;33m', numero[nn])







                        # Resposta do Guanabara



cont =  ('Zero', 'Um', 'Dois', 'Treiz', 'Quatro', 'Cinco', 'Seis',
          'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze',
          'Catoze', 'Quinze', 'Dizesseis', 'Dizessete', 'Dezoito', 'Dizenove', 'Vinte')
while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if 0 <= num <= 20:
        break
    print('Tente novamente. ', end='')
print(f'Você digitou o número {cont[num]}')




                    # Resposta do Desafio

while True:
    numero = ('Zero', 'Um', 'Dois', 'Treiz', 'Quatro', 'Cinco', 'Seis',
              'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze',
              'Catoze', 'Quinze', 'Dizesseis', 'Dizessete', 'Dezoito', 'Dizenove', 'Vinte')
    nn = -1
    while nn < 0 or nn > 20:
        nn = int(input('\033[1;35m Digite um Numero entre 0 e 20: '))
    print(numero[nn])
    rsp = ' '
    while rsp not in 'SN':
        rsp = str(input('Que continua [S/N]: ')).strip().upper()[0]
    if rsp =='N':
        break
