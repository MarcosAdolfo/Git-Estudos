from random import randint
xt = c = 0
nr = 10
I = randint(0, 10)
II = randint(0, 10)
III = randint(0, 10)
IV = randint(0, 10)
V = randint(0, 10)
num = (I, II, III, IV, V)
while True:
    xt = num.count(c)
    if xt >= 1:
        break
    c += 1
while True:
    xt = num.count(nr)
    if xt >= 1:
        break
    nr -= 1
print(f'\033[1;36m Lista de numeros: {num}')
print(f'\033[1;35m Menor Numero: {c}')
print(f'\033[1;34m Maior Numero: {nr}')





                                            # Resposta do Guanabara

#from random import randinr
numeros = (randint(1 , 10), randint(1 , 10), randint(1 , 10),
     randint(1, 10), randint(1 , 10))
print('Os valores sorteados foram: ', end='')
for n in numeros:
    print(f'{n} ', end='')
print(f'\nO maior valor sorteado foi {max(numeros)}')
print(f'O menor valor sorteado foi {min(numeros)}')
