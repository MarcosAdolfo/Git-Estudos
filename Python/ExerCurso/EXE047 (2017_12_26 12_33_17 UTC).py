from random import randint
for p in range(0, 50+1, 2):
    n = randint(30,37)
    print('\033[1;{}m.{}'.format(n, p), end=' ')
