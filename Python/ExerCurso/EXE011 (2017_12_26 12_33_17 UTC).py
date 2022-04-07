At = float(input('\033[1;35m Altura da sua Parede? '))
La = float(input('\033[1;35m A lagura da sua parede? '))
area = At * La
print('\033[1;0m A altura desta parede é {}{:.3f}m\033[m ea lagura é {}{:.3f}m\033[m a area ede {}{:.3f}m \033[m \n Vão ser necessario {}{:.3f}\033[mbaldes de tinta que cubra 2m²'.format('\033[1;34m', At, '\033[1;33m', La, '\033[1;32m', area, '\033[1;31m', area / 2))
