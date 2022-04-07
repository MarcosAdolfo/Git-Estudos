import math
import emoji
import random
import pygame

# Raiz do Numero (

print('.' * 34)

num = float(input('Digite um Numero:'))
print('-'*15,'{}'.format(math.floor(num)), '-'*15)
raiz = math.sqrt(num)
print(emoji.emojize(':large_blue_diamond: A raiz de {} é {:.2f} :large_blue_diamond: '.format(num, raiz)))

print('.' * 34)

# )

# Numero Aleatorio(

print('|'*10)

n1 = random.randint(1, 1000)
print(emoji.emojize(':small_blue_diamond: {}'.format(n1)))

print('|'*10)

# )

#Hiportenusa (

print('>'*34)

co = float(input('Comprimento do Cateto Oposto'))
ca = float(input('Cateto Adjacente'))
hi = (co ** 2 + ca ** 2) ** (1/2)
print(emoji.emojize(':ledger: A Hiportenusa é {:.2f}'.format(math.sqrt(hi))))

print('<'*34)

#  )

#Seno Cosseno Tangente (

print('/'*34)

sct = float(input('Ângulo:'))
seno = math.sin(math.radians(sct))
print(emoji.emojize(':books: O ângulo de {} tem o Seno de {:.2f}'.format(sct, seno)))
cosseno = math.cos(math.radians(sct))
print(emoji.emojize(':books: O ângulo de {} tem o Cosseno de {:.2f}'.format(sct, cosseno)))
tangente = math.tan(math.radians(sct))
print(emoji.emojize(':books: O ângulo de {} tem a Tangent de {:.2f})'.format(sct, tangente)))

print('/'*34)

#   )

#Nomes Aleatorios (

print('\/'*34)

no1 = input('Primeiro Nome')
no2 = input('Segundo Nome')
no3 = input('Terceiro Nome')
no4 = input('Quarto Nome')
nos = [no1, no2, no3, no4]
print(emoji.emojize(' O escolido Foi :crown: {} '.format(random.choice(nos))))

print('\/'*34)

#  )

# Sortendo uma Ordem na lista  (
print('^'*74)

random.shuffle(nos)
print(emoji.emojize('A lista de Apresentação é :page_facing_up: {}  '.format(nos)))

print('^'*74)
#  )

#Tocando MP3  (

print('='*34)

print('-'*15, emoji.emojize(':musical_note:'), '-'*15)

pygame.mixer.init()
pygame.mixer.music.load('nilow.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()

print('='*34)

#  )

print(emoji.emojize("OK :heavy_check_mark:", use_aliases=True))

