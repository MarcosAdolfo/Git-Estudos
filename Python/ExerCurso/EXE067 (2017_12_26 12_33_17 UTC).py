while True:
    n = int(input('\033[1;34m Digite um numero para saber a tabuada: '))
    print(f'\033[1;37m{n:-^30}')
    for c in range(1, 10+1):
        print(f'\033[1;35m {n} x {c} = {n * c}')
    print('\033[1;37m-' * 30)
    res = input('\033[1;36m Que continua [s/n]').strip().upper()[0]
    print('\033[1;37m-'*30)
    if res == 'N':
        break
print('\033[1;31mFim')
