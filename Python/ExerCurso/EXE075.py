var = (int(input('\033[1;35mDigite um numero: ')), int(input('Digite um numero: ')), int(input('Digite um numero: ')), int(input('Digite um numero: ')))
tre = nov = np = 0
print('Você digitou os valores:', end='')
for c in var:
    print(f'\033[1;33m {c} ', end='')
print(f'\nO valor 9 apareceu {var.count(9)}')
if var.count(3) >= 1:
    tre = var.index(3)+1
print(f'O valor 3 aparece na posição {tre}')
print('Os valores pares foram:', end=' ')
for n in var:
    if n % 2 == 0:
        np += 1
        print(n, end=' ' )
if np == 0:
    print('Não a valores pares')










                                    # Resposta do Guanabara


num = (int(input('\nDigite um numero: ')),
       int(input('Digite outro numero: ')),
       int(input('Digite mais um numero: ')),
       int(input('Digite o útimo número: ')))
print(f'Você digitou os valores {num}')
print(f'O valor 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'O valor 3 apareceu na {num.index(3)}ª posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição')
print('Os valores pares digitados foram ', end='')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')
