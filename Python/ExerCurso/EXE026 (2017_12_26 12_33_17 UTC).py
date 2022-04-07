fra = str(input('\033[1;33;47m Digite sua frase ')).strip().lower()

print('\033[1;33;47m Sua frase é {}'.format(fra.title()))
print('\033[1;33;47m Sua frase te {} letra A'.format(fra.count('a')))
print('\033[1;33;47m A primeira ves que a letra A aparece é {}'.format(fra.find('a') + 1))
print('\033[1;33;47m A utima ves que a letra A aparecel é {}'.format(fra.rfind('a') + 1))
