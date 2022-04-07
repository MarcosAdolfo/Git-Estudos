s = 0
con = 0
for c in range(1, 7):
    nu = int(input('\033[1;37mDigite o {}° valor:'.format(c)))
    if nu % 2 == 0:
        s += nu
        con += 1
print('\033[1;34m A soma dos {} numero pares é {}'.format(con, s))
