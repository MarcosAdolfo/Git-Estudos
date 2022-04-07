n = int(input('\033[1;33m Digite um Numero: '))
print('\033[1;35m A tabuada de {} é:'.format(n))
for c in range(1, 11):
    rs = n * c
    print('\033[1;36m {} x {} = {}'.format(n, c, rs))
