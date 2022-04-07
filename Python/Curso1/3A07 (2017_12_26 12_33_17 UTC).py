import math

n1=int(input('Um Numero'))
print('seu numero é {} é seu antecessor é {} é seu sucessor é {}'.format(n1, n1-1, n1+1))
print(' O dobro do seu numero é {} o triplo é {} ia raiz quadrada é {:.2f}'.format(n1*2, n1*3, math.sqrt(n1)))
# Tabuada
print('='*27)
print('A tabuada do Numero {} é  \n {} x 1 = {}   \n {} x 2 = {}   \n {} x 3 = {}   \n {} x 4 = {}   \n {} x 5 = {}   \n {} x 6 = {}   \n {} x 7 = {}    \n {} x 8 = {}    \n {} x 9 = {}'.format(n1, n1, (n1*1), n1, (n1*2), n1, (n1*3), n1, (n1*4), n1, (n1*5), n1, (n1*6), n1, (n1*7), n1, (n1*8), n1, (n1*9) ))
print('=' * 27)

nt1=float(input('Primeira Nota'))
nt2=float(input('Segunda Nota'))
nt3=float(input('Tecera Nota'))
nt4=float(input('Quarta Nota '))
med=(nt1+nt2+nt3+nt4)/4

print('+'*28)
print('Sua media é {:.2f} \n Sua Primeira Nota é {:.2f} \n Sua Segunda Nota é {:.2f} \n Sua Teceira Nota é {:.2f} \n Sua Quarta Nota é {:.2f}'.format(med, nt1, nt2, nt3, nt4))
print('+'*28)

md=float(input('Sua Autura Em Metros'))
print('Sua Autura em Metros é {}m em Centimetros é {}cm e Milimetros {}mm'.format(md, md*100, md*1000))

din=float(input('Dineiro que voce possui '))
print('O seu Dinheiro R${:.2f} convertido em dolares é {:.2f}$'.format(din, din/3.25))

at=float(input('Altura da Parede'))
la=float(input('Largura da sua parede'))
print('Sua Parede tem uma altura de {:.3f}m é uma largura de {:.3f}m é uma area de {:.3f}m² \n Voce vai precisa de {} latas de tinta que cubra 2m² '.format(at, la, (at*la), math.ceil(at*la/2)))

pre=float(input('Preço do Produto R$'))
print('O preço do Produto A vista é {:.2f} com o desconto de 15% fica {:.2f}'.format(pre, pre - (pre * 15) / 100))
print('O preço do Produto Pacelado é {:.2f} com o acrecimo de 5% fica {:.2f}'.format(pre, pre + (pre * 5) / 100))
