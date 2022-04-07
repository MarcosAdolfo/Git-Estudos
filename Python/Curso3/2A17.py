num = [2, 5, 9, 2, 1]
print(num)
num[2] = 3 # O valor da posição 2 vai ser trocado por 3
print(num) # O nove sera trocado pelo 3
num.append(7) # ADD o valor 7 na lista
print(num)
num.sort() #Coloca os valores em ordem
print(num)
num.sort(reverse=True) # Coloca os valores em ordem decrecente
print(num)
print(f'Essa lista tem {len(num)} elementos.') #Mostra o tamanho da lista
num.insert(2, 0) # ADD o valor 0 na posição 2 e reorganisa
print(num) # O zero vai ficar entre 5 e 3
num.pop() # remover o utimo valor
print(num) # O valor 1 foi removido
num.pop(1) # Remover o valor na posição 1
print(num) # O valor 5 foi removido
num.remove(2) # Remover o primeiro valor 2 da lista
print(num) # Remove o 2
if 4 in num: #Checa se o valor enziste na lista antes de dar o remove()
    num.remove(4) #Remove o valor 4
else:
    print('Não achei o número 4')
valores = []
valores.append(5)
valores.append(9)
valores.append(4)
print(valores)
for v in valores:
    print(f'{v}...')
for c, v in enumerate(valores):
    print(f'{v} esta na posição {c}')
print('Cheguei ao final da lista')
valo = []
for cont in range(0, 5):
    valo.append(int(input('Digite um valor: ')))
print(valo)
a = [2, 3, 4, 7]
b = a # Ligação entre lista
b[2] = 8 # Valor da posição 2 vai ser trocador por 8 nas duas listas
print(f'Lista A: {a}')
print(f'Lista B: {b}')

a = [2, 3, 4, 7]
b = a[:] # Cria uma copia dos valores da lista
b[2] = 8 # Valor da posição 2 vai ser trocador por 8 na lista b
print(f'Lista A: {a}')
print(f'Lista B: {b}')

