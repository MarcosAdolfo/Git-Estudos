som = 0
con = 0
for n in range(1, 501, 2):
    if n % 3 == 0:
        con = con + 1
        som += n
print('\033[1;35m A soma de todos os {} valores solicitados é {}'.format(con, som))
