from ExerCurso.EXE115.Texto import EditTXT, VerificaTXT, SalvaTXT
from time import sleep

VTXT = VerificaTXT
EDTXT = EditTXT
STXT = SalvaTXT

requi = ('1', '2', '3', 'sair', 'exit', 'cadastra', 'cadastro', 'consuta') # Todas novas opição add no fim para n muda a orden das ops


while True:

    EDTXT.titulo('Bem vindo', '=', (6, 3, 3),3)

    EDTXT.menu(('Cadastro', 'Consuta', 'Sair'),'num','3','4')

    while True:

        opic = VTXT.Verificado(EDTXT.texto('Escolha uma Opição:', 6, False), requi)
        print('')

        if opic:

            #Cadastro
            while True:
                if opic[1] == requi[0] or opic[1] == requi[5] or opic[1] == requi[6]:

                    EDTXT.titulo('(01) Cadastro', '-', (5, 3, 3), 2)

                    da = VTXT.quest('Nome', 'Idade')
                    d = (da['Nome'], da['Idade'], 'Anos')
                    erc = STXT.salvar(d, 'Cadastro.txt')
                    sleep(0.3)

                    if erc:
                        EDTXT.texto(f'{da["Nome"]} Foi cadastrado com sucerso!', 5)
                        print(EDTXT.texto('-', 3, False) * 60)
                        break
                    else:
                        EDTXT.texto('Erro! Os campos não podem fica em Branco!', 1)
                    sleep(1.5)

                else:
                    break

            #Consuta
            if opic[1] == requi[1] or opic[1] == requi[7]:

                EDTXT.titulo('(02) Consuta', '-', (3, 5, 5), 2)

                EDTXT.texto('Consutando...', 4)
                sleep(2)

                print('')

                a = STXT.ler('Cadastro.txt', False)

                for i in a:
                    I = str(i)
                    nome = I[:I.find(' ')].replace('-', ' ')
                    idade = I[I.find(' '):].replace('\n', '')
                    print(f'{EditTXT.texto(nome, "3", False):<50}', end='  ')
                    print(f'{EditTXT.texto(idade, "4", False):>3}')
                    sleep(0.2)

                print(EDTXT.texto('-', 5, False) * 60)

            break

        else:
            EDTXT.texto('Ops.. Tente uma Opição Valida!\n', 7)

    #Sair
    if opic[1] in requi[2:5]:
        EDTXT.titulo('(03) Saindo', '-', (1, 3, 3), 2)
        sleep(0.5)
        EDTXT.texto('Bay bay!!!', 1)
        break
