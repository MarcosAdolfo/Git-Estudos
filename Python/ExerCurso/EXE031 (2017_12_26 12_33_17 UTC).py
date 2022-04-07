dis = float(input('\033[1;35m Distansia em Km para aviagem '))
if dis <= 200:
    print('\033[1;31m Sua Passagen vai custar R${:.2f}'.format(dis * 0.50))
else:
    print('\033[1;31m Sua passagen vai custar R${:.2f} '.format(dis * 0.45))
