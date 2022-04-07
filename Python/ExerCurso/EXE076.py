v = p = 0
pr = ('Glok', 3000, 'H&K SGP', 40000, 'Imbel 1911', 2500, 'AWM', 38000, 'Barret', 60000, 'IA2', 14000, 'Mp5', 5000)
print('\033[1;33m=' * 50)
print('\033[1;32m{:.^50}'.format('LISTAGEM DE PREÇO'))
print('\033[1;33m=' * 50)
while v < len(pr):
    print('\033[1;32m{:.<40}'.format(pr[v]), end='')
    v += 2
    print(f'R${pr[p + 1]:>7.2f}')
    p += 2
print('\033[1;33m=' * 50)





print('\033[1;35m')
                                    # Resposta do Guanabara

listagem = ('Lapis', 1.75,
            'Borracha', 2,
            'Caderno', 15.90,
            'Estojo', 25,
            'Transferidor', 4.20,
            'Compasso', 9.99,
            'Mochila', 120.32,
            'Canetas', 22.30,
            'Livros', 34.90)
print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' * 40)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R${listagem[pos]:>7.2f}')
print('-' * 40)
