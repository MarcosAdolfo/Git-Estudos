ver = int(input('\033[1;30;41m Qual A velocidade do carro? '))
if ver > 80:
    print('\033[1;31m Voce Foi mutado por utrapaça a velocidade permitida de 80Km ')
    print('\033[1;31m Sua velocidade é de {}Km e sua Muata é R${:.2f}'.format(ver, (ver - 80)* 7))
else:
    print('\033[1;36m Boa viagem!')
