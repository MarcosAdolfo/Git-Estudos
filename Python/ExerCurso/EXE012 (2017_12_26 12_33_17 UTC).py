p1 = float(input('\033[1;37m Digite o preço de um produto '))
des = (p1 * 5 / 100)
print('\033[1;33m O preço do produto é {} com o desconto de 5% fica {}'.format(p1, p1 - des))
