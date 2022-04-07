def leint(n):
    """
    -> Faz amesma função do input so que so asseita numeros inteiros
    :param n: Pergunta Que vai ser realizada
    :return: Retona o valor ser for um nuero inteiro
    """
    while True:
        num = str(input(n))
        if num.isnumeric():
            num = int(num)
            break
        else:
            print('\033[1;31mDigite apenas nueros inteiros!')
    return num


n = leint('\033[1;35mDigite um Numero Inteiro')
print(f'Você acabol de digitar o número: \033[1;34m{n}')






print('\033[1;30m')



                                # Resposta do Guanabara

def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[1;31mERRO! Digite um número inteiro válido.\033[m')
        if ok:
            break
    return valor


# Programa principal
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
