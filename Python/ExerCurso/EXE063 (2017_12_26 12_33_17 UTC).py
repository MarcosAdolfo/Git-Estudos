n = int(input('\033[1;37m Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
print('\033[1;34m{} -> {} '.format(t1, t2), end='')
cot = 3
while cot <= n:
    t3 = t1 + t2
    print(' -> {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    cot += 1
print('\033[1;31m ->Fim')
