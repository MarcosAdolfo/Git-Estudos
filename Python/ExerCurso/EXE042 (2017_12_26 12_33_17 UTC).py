n1 = float(input('\033[1;30m Primeiro Segmento '))
n2 = float(input('\033[1;30m Sugundo Segmento '))
n3 = float(input('\033[1;30m Terseiro Segmento '))
if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n2 + n1:
    print('\033[1;35m O seu Triângulo é ', end='')
    if n1 == n2 == n3:
        print('\033[1;30;44m Equilátero')
    elif n1 == n2 or n1 == n3 or n2 == n3:
        print('\033[1;30;43m Isósceles')
    else:
        print('\033[1;30;46m Escaleno ')
else:
    print('\033[1;31m Os segmentos não forma um triângulo ')
