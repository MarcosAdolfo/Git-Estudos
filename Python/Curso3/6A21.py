#help()                                  # Ajuda interativa - Mostra um manual  ' quit ' para sair
help(print)                              # Mostra uma 'manual' sobre o print
print(input.__doc__)                     # Quase amesma coisa do help(input) so que diferente


def contador(i, f, p):
                                        # Quando da help() naminha função o que vai aparecer e oque esta entre (""" Ola """)
    """
    -> Faz uma contagem e mostra na tela.
    :param i: Início da contagem
    :param f: Fim da contagem
    :param p: Passo da contagem
    :return: Sem retorno

    """
    c = i
    while c <= f:
        print(f'{c}', end=' ')
        c += p
    print('FIM!')


contador(0, 100, 10)
help(contador)                          # Mostra o manual da minha Função que eu defimi entre AS """ """
def somar(a=0, b=0, c=0):               # Caso não seija passado os valores dos parametros ele vai usa o valor ja defnido os valores dos parametros o picionais
    s = a + b + c
    print(f'A soma vale{s}')


somar(3, 2, 5)
somar(8, 4)
somar(a=4, c=5)


def test():
    x = 8
    print(f'Na função teste, n vale {n}')   # n é uma variavel global
    print(f'Na função teste x vale {x}')    # x é uma variavel local


# Programa Pricinpal
n = 2
print(f'No programa principal, n vale {n}')
test()
print(f'No programa principal, n vale {"x"}')   # a variavel x vai dar erro pq ela so existe dentro da função test


def teste(b):
    a = 8                                       # Variavel local, o valo não vai ser trocado e sim vai se criado uma nova variavel 'a' local
    b += 4
    c = 2
    print(f'A dentro vale {a}')                 # A dentro vale 8
    print(f'B dentro vale {b}')                 # B dentro vale 9
    print(f'C dentro vale {c}')                 # C dentro vale 2

a = 5
teste(a)                                        # vai chama a função teste e mostra os prints de sima
print(f'A fora vale {a}\n')                     # A fora vale 5


def tt(b):
    global a                                    # Declara a com variavel global assim não vai criar uma variavel local 'a' e sim usa a variavel global existente
    a = 2
    b += 4
    c = 1
    print(f'A dentro vale {a}')                 # A dentro vale 2
    print(f'B dentro vale {b}')                 # B dentro vale 8
    print(f'C dentro vale {c}')                 # C dentro vale 1


a = 4
tt(a)
print(f'A fora vale {a}')                       # A fora vale 2 pq eu mudei a variavel 'a' global naminha função


def somar(a=0, b=0, c=0):
    s = a + b + c
    return s                                    # Faiz o valor retorna a sim não precisa utilisa o print


resp = somar(3, 2, 5)                           # resp vai reseber o valor da função somar()
respB = somar(1, 3)
print(f'\n resposta = {resp} resposta de B é {respB}\n')  # resposta = 10 resposta de B é 4


def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


n = int(input('Digite um número: '))
print(f'O fatorial de {n} é igual a {fatorial(n)}')
f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'Os resultados são {f1}, {f2} e {f3}\n')


def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False


num = int(input('Digite um número par: '))
if par(num):
    print('É par!')
else:
    print('Não é par!')
