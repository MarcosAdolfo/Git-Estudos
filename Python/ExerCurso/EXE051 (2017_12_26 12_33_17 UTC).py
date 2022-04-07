a1 = int(input('\033[1;30m Primeiro termo:'))
r = int(input('Razão:'))
t = a1 + (10 -1) * r
for c in range(a1, t + r, r):
    print('\033[1;34m {}'.format(c), end=' ')
