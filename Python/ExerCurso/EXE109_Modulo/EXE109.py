import moeda

numero = str(input('\033[1;35mDigite o preço: R$'))
print(f'\033[1;33mA metade de {moeda.moedas(numero)} é {moeda.moedas(numero, "metade")}')
print(f'\033[1;33mO dobro de {moeda.moedas(numero)} é {moeda.moedas(numero, "dobro")}')
print(f'Aumentando 10% temos {moeda.moedas(numero, "almentar", porc=10)}')
print(f'Reduzindo 25% temos {moeda.moedas(numero, "diminuir", moe="R$", porc=25, formata=True)}')





print('\033[1;34m')



                                # Resposta do Guanabara

import moeda

p = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.moeda(p)} é {moeda.me(p, True)}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.do(p, True)}')
print(f'Aumentando 10%, temos {moeda.al(p, 10, True)}')
print(f'Reduzindo 13%, temos {moeda.di(p, 13, True)}')
