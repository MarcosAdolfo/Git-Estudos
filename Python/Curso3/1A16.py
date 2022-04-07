# Tuplas
lanche = ('hanbúrguer', 'suco', 'pizza', 'pudim')
# Tuplas são imutáveis
print(lanche)
print(lanche[2]) #Pizza
print(lanche[-1]) # Pudim
print(lanche[1:3]) #Suco Pizza   #... 1:  ...:2  ...-2
print(lanche[-2:]) #Pizza pudim
print(lanche[1:]) #Suco Pizza Pudim
print(len(lanche))
for comida in lanche:
    print(f'Eu vou comer {comida}')

for cont in range(0, len(lanche)):
    print(f'Eu vou comer{lanche[cont]}')

for pos, comida in enumerate(lanche):
    print(f'eu Vou cormer{comida} na posição{pos}')

print('Comi pra caramba!')

print(sorted(lanche))

a = (2, 5, 4)
b = (5, 2, 1, 2)
c = a + b
print(c)
print(c.count(5)) #em c tem 2 - 5
print(c.index(2)) #Posição onde o 2 estar
pessoa = ('gustavo', 39, 'M', 99.88)
print(pessoa)
del(pessoa) #del apaga a Tupla
