#1  ()
#2  **
#3 * / // %
#4 + -

n1 = int(input('Um numero'))
n2 = int(input('outro numero'))
s = n1+n2
m = n1*n2
d = n1/n2
ra = n1**n2
print('A soma de {} + {} = {} \n A mutiplicação é {} \n A divisão é {} '.format(n1, n2, s, m, d))
print('A potencia {}'.format(ra))
print('O resutado de tudo é {},{},{} é {}'.format(s, m, d, ra))
print('resutado {} +  o resutado da divisão {} veses A Raiz quadrada {} e imgual a {}'.format(s, d, ra, s+d*ra))

