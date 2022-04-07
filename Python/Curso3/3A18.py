p = list()          # cria uma lista
p.append('Gustavo') # ADD Gustavo na lista
p.append(40)        # ADD '40' na lista
print(p)            # Da um print na lista no caso - ['Gustavo', 40]
t = []              # cria uma lista
t.append(p)         # ADD alista 'p' na lista 't' - [['Gustavo', 40]]
print(t)            # [['Gustavo', 40]]
p[0] = 'Maria'      # troca o valor da posição '0'da lista 'p' ficando Maria por Gustavo - [Maria, 40]
p[1] = 22           # troca o 40 por 22 na lista 'p' - [Maria, 22]
t.append(p)         # ADD alista 'p' denovo
print(t)            # [['Maria', 22], ['Maria', 22]]

''' No esenplo de cima alista ser repete duas vs ingual pq quando da um 
'.append(Varia)' en otra lista cria uma ligação entre as estruturas 
quando muda uma muda a outra tam bem '''

gt = list()         # cria uma lista
gt.append('Gustavo')# ADD Gustavo na lista
gt.append(40)       # ADD '40' na lista
print(gt)           # Da um print na lista no caso - ['Gustavo', 40]
g = []              # cria uma lista
g.append(gt[:])     # [:] cria uma copia da lista 'gt'
gt[0] = 'Maria'     # Troca o valor de 0-Gustavo- por Maria
gt[1] = 22          # Troca 40 por 22
print(gt)           # ['Maria', 22]
g.append(gt[:])     # ADD uma copia de 'gt' na lista 'g'
print(g)            # [['Gustavo'], ['Maria', 22]]

''' Neste caso não se repete os valores da lista duas veses pq quando se dar '.append(varia[:])' 
esta criando uma copia da 'Varia' en questão sem criar qualque ligação jaque e so uma copia 
assim pode muda os valores depois, sem autera a copia '''

gg = [['João', 29], ['Ana', 18], ['Maria', 23]] # Cria uma Lista com sub listas
print(gg)                                       # [['João', 29], ['Ana', 18], ['Maria', 23]]
print(gg[0], gg[0][0], gg[2][1])                # gg[0] = ['João', 29] | gg[0][0] = João | gg[2][1] = 23
for n in gg:                                    #
    print(n)                                    # Vai printa um valor para cada valor da lista - ['João', 29] ['Ana', 18] ['Maria', 23] um enbaixo do outro
for n in gg:                                    #
    print(f'{n[0]} tem {n[1]} anos de idade.')  # vai printa n[0]-'valor da lista'- tem n[1]-'valor da lista'- anos de idade'
no = []
dado = list()
totmai = totmen = 0
for c in range(0,3):
    dado.append(str(input('Nome')))
    dado.append(int(input('Idade')))
    no.append(dado[:])                          #ADD a copia da lista 'dado' na lista 'no'
    dado.clear()                                #deleta a lista 'dado'
print(no)

 # Verifica se é maior ou menor de idade

for c in no:
    if c[1] >= 21:
        print(f'{c[0]} é maior de idade')
        totmai += 1
    else:
        print(f'{c[0]} é menor de idade')
        totmen += 1
print(f'Temos {totmai} maioes e {totmen} menores de Idade.')
