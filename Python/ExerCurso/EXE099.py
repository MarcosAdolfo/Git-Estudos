from time import sleep


def maior(*num):
    sleep(2)
    print('\033[1;35m=-' * 30)
    print('\033[1;33m Analisando os Valores...')
    ma = 0
    sleep(2)
    for c in num:
        sleep(0.5)
        print(f'  {c}', end='', flush=True)
        if c > ma:
            ma = c
    print(f'  São {len(num)} valores ao todo.')
    sleep(1.5)
    print(f'  O maior Valor é {ma}')
    print('\033[1;35m=-' * 30)


maior(10, 2, 9, 4, 5)
maior(6, 9, 7, 8, 3, 1, 5, 4, 0, 40, 50, 32, 450, 0)
maior()



print('\033[1;30m')

                                # Resposta do Guanabara

from time import sleep


def maior(*núm):
    cont = maior = 0
    print('-=' * 30)
    print('Analisando os valores passados... ')
    for valor in núm:
        print(f'{valor} ', end='', flush=True)
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')


# Programa Principal
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
