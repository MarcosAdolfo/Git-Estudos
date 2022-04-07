sg1 = float(input('\033[7;30m primeiro segmento'))
sg2 = float(input('\033[7;30m Segundo segmento'))
sg3 = float(input('\033[7;30m Terseiro Segmento'))

if sg1 < sg2 + sg3 and sg2 < sg1 + sg3 and sg3 < sg2 + sg1:
    print('\033[1;35;40m Os segmentos pode forma um triangulo')
else:
    print('\033[1;31;40m Os segmentos não forma um triangulo')
