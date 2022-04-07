v1 = int(input('\033[1;34m Digite um valor '))
v2 = int(input('\033[1;36m Digite outro valor '))
v3 = int(input('\033[1;30m Digite outro valor '))
v4 = int(input('\033[1;35m Digite o Quarto valor '))
meno = v1
if v2 < v1 and v2 < v3 and v2 < v4:
    meno = v2
if v3 < v1 and v3 < v2 and v3 < v4:
    meno = v3
if v4 < v1 and v4 < v2 and v4 < v3:
    meno = v4
print('\033[1;33m menor numero é {}'.format(meno))
maio = v4
if v1 > v4 and v1 > v2 and v1 > v3:
    maio = v1
if v2 > v4 and v2 > v3 and v2 > v1:
    maio = v2
if v3 > v4 and v3 > v1 and v3 > v2:
    maio = v3
print('\033[1;33m maio numero é {}'.format(maio))
