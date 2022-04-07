Vcasa = float(input('\033[1;35m Valor da casa? '))
sa = float(input('\033[1;35m Seu Salario? '))
qt = int(input('\033[1;35m Em Quantos Anos voce vai pagar? '))
pax = Vcasa / (qt * 12)
val = (sa * 30 / 100)
if pax <= val:
    print('\033[7;30m O valor da casa é \033[1;33;40mR${:.2f} \033[7;30m vai ser paga em \033[1;33;40m{:.0f}anos \033[7;30m ea prestação é \033[1;33;40mR${:.2f} '.format(Vcasa, qt, pax))

else:
    print('\033[1;31m Seu salario de {} não é suficiente para esta casa'.format(sa))
