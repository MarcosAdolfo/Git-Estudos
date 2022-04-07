valo = [[], []]
v = 0
for c in range(7):
    v = int(input(f'\033[1;34m Digite o {c + 1}° valor: '))
    if v % 2 == 0:
        valo[0].append(v)
    else:
        valo[1].append(v)
print('\033[1;36m-=-' * 30)
valo[0].sort()
valo[1].sort()
print(f'\033[1;35m Os valores Pares são: {valo[0]}')
print(f'\033[1;33m Os valores impares são: {valo[1]}')




print('\033[1;33m')

                                    # Resposta do Guanabara
#Imgual aminha