import moeda

numero = float(input('\033[1;35mDigite o preço: R$'))
dobro = moeda.dobro(numero)
metade = moeda.metade(numero)
alme = moeda.almentar(numero)
print(f'\033[1;33mA metade de R${numero} é R${metade}')
print(f'\033[1;33mO dobro de R${numero} é R${dobro}')
print(f'Aumentando 10%, temos R${alme}')





print('\033[1;34m')



                                # Resposta do Guanabara

import moeda

p = float(input('Digite o preço: R$'))
print(f'A metade de R${p} é R${moeda.me(p)}')
print(f'O dobro de R${p} é R${moeda.do(p)}')
print(f'Aumentando 10%, temos R${moeda.al(p, 10)}')
