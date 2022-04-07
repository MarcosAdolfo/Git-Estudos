import moeda

numero = str(input('\033[1;35mDigite o preço: R$'))
print(f'\033[1;33mA metade de R${numero} é {moeda.metade(numero)}')
print(f'\033[1;33mO dobro de R${numero} é {moeda.dobro(numero)}')
print(f'Aumentando 10% temos {moeda.almentar(numero, 10)}')





print('\033[1;34m')



                                # Resposta do Guanabara

import moeda

p = float(input('Digite o preço: R$'))
print(f'A metade de R${moeda.moeda(p)} é R${moeda.moeda(moeda.me(p))}')
print(f'O dobro de R${moeda.moeda(p)} é R${moeda.moeda(moeda.do(p))}')
print(f'Aumentando 10%, temos R${moeda.moeda(moeda.al(p, 10))}')
