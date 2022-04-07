res = ' '
lis = []
while res != 'N':
    res = ' '
    lis.append(int(input('\033[1;35m Digite um numero: ')))
    while res not in 'SN':
        res = str(input('\033[1;34m Que comtinuar? Sim ou Não ')).strip().upper()[0]
if 5 in lis:
    rp = 'Foi encomtrado na lista'
else:
    rp = 'Não foi encomtrado na lista'
lis.sort(reverse=True)
print('\033[1;35m==+'*30, f'\033[1;34m\n Foram digitados {len(lis)} Numeros \n {lis} \n O valor 5 {rp}')




print('\033[1;33m')
                                    # Resposta do Guanabara

valores = []
while True:
    valores.append(int(input('Digite um valor: ')))
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'Você digitou {len(valores)} elementos.')
valores.sort(reverse=True)
print(f'Os valores em ordem decrescente são {valores}')
if 5 in valores:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não foi encontrado na lista!')
