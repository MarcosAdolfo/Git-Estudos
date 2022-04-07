import random
from time import sleep
import emoji
from datetime import date


n1 = float(input('Primeira nota'))
n2 = float(input('Segunda Nota'))
n = (n1 + n2)/2
print('A sua Media é {:.2f}'.format(n))
if n >= 6.0:
    print('Sua Media Foi Boa! Parabéns!')
else:
    print('Sua nota foi ruin! Esdude Mais!')

print('_-_-' * 10, emoji.emojize(':video_game:'), '_-_-'*10)

npc = random.randint(0, 10)
usu = int(input('Tente adivinha o numero que eu esto pensando de 1 a 10 '))
print('PROCESSANDO...')
sleep(2.5)
if usu == npc:
    print('Muinto Bem! O numero que eu estava Pensando era este Mesmo O {}. Você é Esperto! Meus Parabens.  '.format(npc))
else:
    print('Não foi desta Ves o numero Que eu estava Pensando era {}. Tente de novo! Você vai Perde mesmo !'.format(npc))

print('-_-_' * 22)

print('')

print('Uma Nova Estrada Foi Construida!')
print('olimite de velocidade é 80Km é ela é de faicha dupla com iluminação propria.')
print('Voce esta indo nesta nova estrada, para Iguagasur no Norte, Falta 200Km para chega e Você Precisa chega antes de 2h.')
moto = int(input('A qual Velocidade você iria?'))
if moto > 80:
    print('Voce estava indo muito rapido e Foi mutado por um Policial por cada Quilometro acima de 80Km, agora você vai te que pagar R${:.2f}'.format((moto-80)*7))
else:
    print('Você chegol atrasada no seu destinho mas você chegol bem e não quebrol nem uma norma de transito,Parabens ! Você é um esenplo!')

nume = int(input('Digite Um numero:'))
va = nume % 2
if va == 0:
    print('Este Numero é Par')
else:
    print('Este Numero é Impar')

print('Você vai faser uma viagen de onibus. \n Cada Passagen custa R$0,50 por cada Quilometro ate 200Km é 0,45 por viagens assima de 200Km')
vir = float(input('Quantos Quilometros você pretende ir'))
if vir <= 200:
    print('Sua Passagem vai custa R${:.2f} para andar {}Km'.format(vir * 0.50, vir))
else:
    print('Sua viagem vai ser assima dos 200Km. O custo da passagem ate {} é de R${:.2f} '.format(vir, vir * 0.45))

nm1 = int(input('Digite um numero:'))
nm2 = int(input('Digite outro numero:'))
nm3 = int(input('Digite outro numero:'))
menor = nm1
if nm2 < nm1 and nm2 < nm3:
    menor = nm2
if nm3 < nm1 and nm3 < nm2:
    menor = nm3
maior = nm1
if nm2 > nm1 and nm2 > nm3:
    maior = nm2
if nm3 > nm1 and nm3 > nm2:
    maior = nm3
print('{} é o maior numero'.format(maior))
print('{} é o menor numero'.format(menor))


sal = float(input('Seu salario é ?'))
if sal > 1250:
    print('Seu almento ede R${:.2F}. Agora seu Salario é {:.2f}'.format((sal * 10 / 100), (sal * 10 / 100) + sal))
else:
    print('Seu almento ede R${:.2f}. Agora seu Salario é {:.2f}'.format((sal * 15 / 100), (sal * 15 / 100) + sal))

ano = int(input('Que ano quer voce quer analisar? 0 para analisa o ano atual'))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('Oano de {} é Bissexto'.format(ano))
else:
    print('O ano {} não é Bissexto'.format(ano))

rt1 = float(input('Primeiro Segmento:'))
rt2 = float(input('Segunda Segmento:'))
rt3 = float(input('Terceiro Segmento:'))
if rt1 < rt2 + rt3 and rt2 < rt1 +rt3 and rt3 < rt1 +rt2:
    print('Os segmentos Podem Formar um Triângulo!')
else:
    print('Os segmentos Não Podem forma um Triângulo!')

