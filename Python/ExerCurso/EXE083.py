pf = pa = 0
n = str(input('\033[1;37mExpressão: '))
for v in range(len(n)):
    if n[v] == '(':
        pf += 1
    elif n[v] == ')':
        pa += 1
if pa == pf:
    print('Expressão coreta!')
else:
    print('Expressão incoreta!')





print('\033[1;33m')

                                    # Resposta do Guanabara

expr = str(input('Digite a expressão: '))
pilha = []
for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')


                                        # Resposta dos Comentarios


exp = str(input('\033[1;35mDigite a expressão: '))
if exp.count('(') == exp.count(')'):
    print('Sua expressão é válida!!')
else:
    print('Sua expressão não é válida')
