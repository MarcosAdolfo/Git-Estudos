maior = 0
menor = 0
for c in range(1, 6):
    peso = float(input('{}° Peso '.format(c)))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(' O maior peso é {} é o meno peso é {} '.format(maior, menor))


# Tentativa

'''
ps = 0
n1 = 0
n2 = 0
n3 = 0
n4 = 0
n5 = 0
for c in range(1, 6):
    peso = float(input('\033[1;34m {}° Peso'.format(c)))
    if c == 1:
        n1 += peso
    if c == 2:
        n2 += peso
    if c == 3:
        n3 += peso
    if c == 4:
        n4 += peso
    if c == 5:
        n5 += peso
if n1 > n2 and n1 > n3 and n1 > n4 and n1 > n5:
    print(n1)
if n2 > n1 and n2 > n3 and n2 > n4 and n2 > n5:
    print(n2)
if n3 > n1 and n3 > n2 and n3 > n4 and n3 > n5:
    print(n3)
if n4 > n1 and n4 > n2 and n4 > n3 and n4 > n5:
    print(n4)
if n5 > n1 and n5 > n2 and n5 > n3 and n5 > n4:
    print(n5)
'''
