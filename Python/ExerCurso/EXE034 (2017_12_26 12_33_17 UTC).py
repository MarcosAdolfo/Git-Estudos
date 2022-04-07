sal = float(input('\033[1;30;43m Digite seu salario '))
if sal > 1250:
    sal1 = sal * 10 / 100
    print('\033[1;33;40m Seu Salario é {} seu aumento é {} seu novo salario é {}'.format(sal, sal1, sal1 + sal))
else:
    sal1 = sal * 15 / 100
    print('\033[7;30m Seu Salario é {} seu aumento é {} seu novo salario é {}'.format(sal, sal1, sal1 + sal))

