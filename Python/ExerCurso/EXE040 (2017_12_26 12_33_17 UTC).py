not1 = float(input('\033[1;33m Primeira nota? '))
not2 = float(input('\033[1;33m Segunda nota? '))
med = (not1 + not2) / 2
if med >= 7:
    print('\033[1;32m Aprovado! Sua media foi muito boar. \n Suas notas foram {:.1f} é {:.1f} é sua media é {:.1f}'.format(not1, not2, med))
elif med < 5:
    print('\033[1;31m Reprovado! sua media foi ruin \n Suas notas foram {:.1f} é {:.1f} é sua media é {:.1f}'.format(not1, not2, med))
elif med == 5 or med < 6.9:
    print('\033[1;35m Recuperação! Sua media não foi suficiente \n Suas notas foram {:.1f} é {:.1f} é sua media é {:.1f}'.format(not1, not2, med))

