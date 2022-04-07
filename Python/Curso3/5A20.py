print('-' * 30)                                 # Da print em uma linha repetidadamente ez: -----------------
print('  CURSO EM VÍDEO  ')                     # Printa 'CURSO EM VÍDEO
print('-' * 30)                                 # -------------------------------
print('-' * 30)
print('  APRENDA PYTHON  ')
print('-' * 30)
print('-' * 30)
print('  GUSTAVO GUANABARA  ')
print('-' * 30)


def lin():                                      # Cria uma Fução, Tipo um novo comando tipo - print - que mostra augo na tela neste caso lin() vai mostra linhas - '-' * 30 -
    print('-' * 30)                             # e oque a função lin vai faser no caso vai mostra uma linha - '-' * 30 - sempre que eu o chamar
                                                # O brigatorio deixa duas linhas depois do 'def'

lin()                                           # Mostra uma linha - '-' * 30 -
print('  CURSO EM VÍDEO  ')
lin()                                           # -------------------------------
print('  APRENDA PYTHON  ')
lin()                                           # -------------------------------
print('  GUSTAVO GUANABARA  ')
lin()                                           # -------------------------------


def titulo(txt):                                # Cria uma Função titulo com o parametro txt
    print('-' * 30)
    print(txt)                                  # Printa o valor do parametro txt
    print('-' * 30)


titulo(' Curso em Video ')                      # Passo 'Curso em Video' como parametro de titulo agora txt vale Curso em Video
titulo(' Python é Muito Bom! ')                 # Vai esecutar a função titulo dando um print na msg que estou passando como parametro
titulo('OI')                                    # vai dar um print em ' OI '
a = 4                                           # a vai valer o valor 4
b = 5
s = a + b                                       # s vai valer asoma do valor 'a' mais 'b'
print(s)                                        # Vai da um print em 's' que e a soma de a + b
a = 1
b = 3
s = a + b
print(s)
a = 8
b = 9
s = a + b
print(s)                                        # 17
def soma(a, b):                                 # Função para soma dois valores
    s = a + b                                   # s recebe o valor da soma dos parametros 'a' e 'b'
    print(s)                                    # Da um print em 's'


soma(8, 9)                                      # Define os valores dos parametros 'a' e 'b' nocaso os novos parametros são 8, 9
soma(1, 3)                                      # O resutado vai ser 4 ou vai dar print no resutado '4'
soma(2, 5)                                      # Vai printar '7'
def soma(b, a):                                 # Faiz amesma coisa do que a um tima função
    print(f'A = {a} B = {b}')                   # Print Formatado
    s = a + b
    print(f'A soma de A + B = {s}')


soma(a=4, b=5)                                  # Posso dise qual parametro recebe qual valor
soma(b=3, a=7)                                  # A = 7 B = 3 \n A soma de A + B = 10
soma(4, 16)                                     # A = 16 B = 4 \n A soma de A + B = 20
def contador(*num):                             # Funçao para receber vareos valores, o a ( * ) antes epara declara um empacotamento aonde não sabe o total aser enserido
    print(num)                                  # Print da função, o desenpacotamento vai joga os valores em uma tupla
    for valor in num:
        print(f'{valor} ', end='')
    print('FIM!')
    tam = len(num)
    print(f' Recebi os valores {num} e são ao todo {tam} números')


contador(2, 3, 5, 4, 2, 0, 0)                   # (2, 3, 5, 4, 2, 0, 0) \n 2 3 5 4 2 0 0 FIM! \n Recebi os valores (2, 3, 5, 4, 2, 0, 0) e são ao todo 7 números
contador(1, 9, 3)
contador(0, 4, 5, 2, 0)
def dobra(lst):                                 # Uma função que receber uma lista
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [0, 5, 4, 2, 0]                       # Lista de valores
dobra(valores)                                  # Função que dobra os valores
print(valores)                                  # [0, 10, 8, 4, 0]

