pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}             #Cria um Dicionário
print(pessoas)                                                      #da um print no Dicionário - {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
print(pessoas['nome'])                                              #da um print no nome - Gustavo
print(f'{pessoas["nome"]} tem {pessoas["idade"]} anos.')            #Gustavo tem 22 anos.
print(pessoas.keys())                                               #da um print nas chaves - dict_keys(['nome', 'sexo', 'idade']
print(pessoas.values())                                             #da um print nos valores - dict_values(['Gustavo', 'M', 22])
print(pessoas.items())                                              #da um print nos items - dict_items([('nome', 'Gustavo'), ('sexo', 'M'), ('idade', 22)])
for k in pessoas.keys():
    print(k)                                                        #nome sexo idade - um em baixo do outro
for v in pessoas.values():
    print(v)                                                        #Gustavo M 22 - um debaixo do outro
for k, v in pessoas.items():
    print(f'{k} = {v}')                                             #nome = Gustavo  sexo = M  idade = 22 - debaixo do otro
del pessoas['sexo']                                                 #Deleta 'sexo' do Dicionário
print(pessoas)                                                      #{'nome': 'Gustavo', 'idade': 22}
pessoas['nome'] = 'Leandro'                                         #Troca os nomes de Gustavo por Leandro
print(pessoas['nome'])                                              # Leandro
pessoas['peso'] = 98.5                                              #ADD Peso na Dicionário
print(pessoas)                                                      #{'nome': 'Leandro', 'idade': 22, 'peso': 98.5}
brasil = []                                                         #cria uma lista
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}                   #Cria um dicionário
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)                                              #ADD o dicionário -estado1- na lista brasil
brasil.append(estado2)                                              #ADD o dicionário -estado2- na lista brasil
print(estado1)                                                      #{'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
print(brasil)                                                       #[{'uf': 'Rio de Janeiro', 'sigla': 'RJ'}, {'uf': 'São Paulo', 'sigla': 'SP'}]
print(brasil[1])                                                    #{'uf': 'São Paulo', 'sigla': 'SP'}
print(brasil[0]['uf'])                                              # Rio de Janeiro
estadots = dict()                                                   #Cria um dicionário
bra = list()                                                        ##cria uma lista
for c in range(3):
    estadots['uf'] = str(input('Unidade Federativa: '))
    estadots['sigla'] = str(input('Sigla do Estado: '))
    bra.append(estadots)
print(bra)                                                          #[{'uf': 'Ceara', 'sigla': 'CE'}, {'uf': 'Ceara', 'sigla': 'CE'}, {'uf': 'Ceara', 'sigla': 'CE'}]

''' No caso de cima os valores ser repete pelo mesmo 
motivo que acontece nas listas então precisa fase uma copia .copy()'''

estado = dict()                                                     #Cria um dicionário
br = list()                                                         #cria uma lista
for c in range(3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    br.append(estado.copy())                                        # Cria uma copia, mesma funcinalidade [:] das listas so que para dicionários
print(br)                                                           #[{'uf': 'Acre', 'sigla': 'AC'}, {'uf': 'Minas', 'sigla': 'MG'}, {'uf': 'Ceara', 'sigla': 'CE'}]
for e in br:
    print(e)
for e in br:
    for k, v in e.items():
        print(f'O Campo {k} tem valor {v}')
for e in br:
    for v in e.values():
        print(v, end=' ')
    print()

