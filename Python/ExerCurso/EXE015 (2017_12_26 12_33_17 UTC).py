km = float(input('\033[1;30;44m Km que o carro rodol:'))
dias = int(input('\033[1;30;44m Dias que o carro ficol alugado'))
tax = (dias * 60) + (km * 0.15)
print('\033[1;37;40m O preço a paga é {:.2f}\033[m'.format(tax))
