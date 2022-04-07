mat = [[], [], []]
lc = 3
cx = 3
for c in range(lc):
    for x in range(cx):
        mat[c].append(int(input(f'\033[1;35mDigite um Valor para [{c},{x}]: ')))
print(f'\033[1;33m {mat[0]} \n {mat[1]} \n {mat[2]}')







print('\033[1;36m')



                                    # Resposta do Guanabara

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}] '))
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
