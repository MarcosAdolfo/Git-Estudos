import math
cap = float(input('\033[1;30;43m Valor do cateto oposto'))
caa = float(input('\033[1;30;43m Valor do cateto adjacente'))
#hip = (cap ** 2 + caa **2) ** (1/2)
hip = math.hypot(cap, caa)
print('\033[1;33;40m A hipotenusa de {} e {} é {:.2f}'.format(cap, caa, hip))

