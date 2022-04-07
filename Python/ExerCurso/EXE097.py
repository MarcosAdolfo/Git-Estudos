def escreva(txt):
    print(f'\033[1;36m{"~" * (len(txt) + 2):^10}')
    print(f'\033[1;35m{txt:^10}')
    print(f'\033[1;36m{"~" * (len(txt) + 2):^10}')


escreva('Ola')
escreva('Python')
escreva('Marcos Adolfo')
escreva('Curso de Python no curso em video')




print('\033[1;33m')


                                # Resposta do Guanabara


def escreva(msg):
    tam = len(msg) + 4
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)


# Programa Principal
escreva('Gustavo Guanabara')
escreva('Curso de Python no YouTube')
escreva('CeV')
