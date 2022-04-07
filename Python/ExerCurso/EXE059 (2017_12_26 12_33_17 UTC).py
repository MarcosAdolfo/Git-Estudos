from time import sleep
ops = 4
res = ''
print('\033[1;33m Iniciando...')
sleep(2)
while ops == 4:
    num1 = float(input('\033[1;34m Primeiro Numero'))
    num2 = float(input('Segundo numero \033[m'))
    ops = 0
    while ops != 5 and ops != 4:
        print('''\033[1;34m
        1 - Soma
        2 - Multiplicar
        3 - Maior
        4 - Novos Números
        5 - Sair do Programa''')
        ops = int(input('Escolha uma das opiçoes:'))
        if ops == 1:
            res = num1 + num2
            print('A soma é:')
        if ops == 2:
            res = num1 * num2
            print('A multiplicação é:')
        if ops == 3:
            if num1 > num2:
                res = num1
            else:
                res = num2
            print('O maior numero é:')
        if ops != 4 and ops != 5:
            sleep(2)
            print('\033[1;36m {}'.format(res))
        if ops == 5:
            print('\033[1;33m encerrando...')
            sleep(2)
        if ops > 5:
            print('\033[1;31mOpção invalida! Tente Denovo')
        if ops != 5:
            print('\033[1;33m Iniciando nova sessão...')
            sleep(5)

# Resposta

n1 = int(input('Primeiro Valor:'))
n2 = int(input('Segundo Valor'))
opção = 0
while opção != 5:
    print('''\033[1;34m
    1 - Somar
    2 - Multiplicar
    3 - Maior
    4 - Novos Números
    5 - Sair do Programa''')
    opção = int(input('>>>Qual é a sua opção? '))
    if opção == 1:
        soma = n1 + n2
        print('A soma de {} + {} é {}'.format(n1, n2, soma))
    elif opção == 2:
        produto = n1 * n2
        print('O resultado de {} X {} é {} '.format(n1, n2, produto))
    elif opção == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Entre {} e {} o maior valor é {}'.format(n1, n2, maior))
    elif opção == 4:
        print('Informe os números novamente:')
        n1 = int(input('Primeiro Valor:'))
        n2 = int(input('Segundo Valor:'))
    elif opção == 5:
        print('\033[1;33mfinalizando...')
        sleep(2)
    else:
        print('\033[1;31m opção inválida. Tente Novamente')
    print('=-=' * 10)
print('fim do programa! Volte sempre!')
