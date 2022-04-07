num = int(input('\033[1;30;46m Digite um numero de 1 a 9999'))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('\033[1;33;46m O numero {} ten \n {} unidade \n {} Dezena \n {} Centena \n {} Milhat'.format(num, u, d, c, m))

