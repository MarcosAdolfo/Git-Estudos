NumIn = 0
NumRe = 0
while True:
    try:
        if NumIn == 0:
            NumIn = int(input('Numero Inteiro: '))
        NumRe = float(input('Numero Real: '))

    except (KeyboardInterrupt):
        print(f' O Numero Inteiro Digitado é {NumIn}')
        print(f' O Numero Real Digitado é {NumRe}')
        break

    except:
        print('\033[1;31m ERRO! \n Verifique o valo digitado!\033[m')

    else:
        break

print(f' O Numero Inteiro Digitado é {NumIn}')
print(f' O Numero Real Digitado é {NumRe}')


                            # Resposta do Guanabara

def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31m ERRO: Por favor, digite um número inteiro válido. \033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[31m Usuário Preferiu não digita esse número. \033[m')
            return 0
        else:
            return n

def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31m ERRO: Por favor, digite um número Real válido. \033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[31m Usuário Preferiu não digita esse número. \033[m')
            return 0
        else:
            return n

n1 = leiaInt('Digite um valor Inteiro:')
n2 = leiaFloat('Digite um valor Real')
print(f'O valor inteiro digitado foi {n1} e o real foi {n2}')
