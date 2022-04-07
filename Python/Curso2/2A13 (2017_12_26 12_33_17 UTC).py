print('\033[1;32m{:=^40}'.format(' oiii '))
for c in range(0, 4):
    print('OI')
print('Fim')

for c in range(10, 0, -1):
    print(c)
print('Fim')

for c in range(1, 10, 2):
    print(c)

n = int(input('Digite um número: '))
for c in range(0, n+1):
    print(c)
print('FIM')

i = int(input('Início: '))
f = int(input('Fim: '))
for c in range(i, f+1):
    print(c)

s = 0
for c in range(0, 4):
    n = int(input('Digite um valor: '))
    s += n
print('A soma de todos os valores foi {}'.format(s))
