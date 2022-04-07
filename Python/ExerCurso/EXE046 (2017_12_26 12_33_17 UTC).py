from time import sleep
print('\033[1;33m{:*^60}'.format(' Fim de Ano '))
co = {0: '\033[1;31m', 1: '\033[1;35m', 2: '\033[1;36m', 3: '\033[1;34m', 4: '\033[1;32m', 5: '\033[1;33m', 6: '\033[1;35m', 7: '\033[1;37m', 8: '\033[1;36m', 9: '\033[1;34m', 10: '\033[1;30m'}
for c in range(10, 0-1, -1):
    print('{}{}'.format(co[c], c))
    sleep(1)
print('{}Feliz {}Ano{} Novo{}!'.format(co[5], co[4], co[2], co[0]))