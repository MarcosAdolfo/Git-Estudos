import random
nm0 = str(input('\033[1;32;40m Primeiro Nome'))
nm1 = str(input('\033[1;32;40m Segundo Nome'))
nm2 = str(input('\033[1;32;40m Terceiro Nome'))
lst = [nm0, nm1, nm2]
esco = random.choice(lst)
print('\033[1;30;42m O escolido foi {}'.format(esco))

