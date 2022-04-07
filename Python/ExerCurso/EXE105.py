def nota(*nota, sit=False):
    """
    --> Ressebe uma quantidade de notas é mostra o maior e menor nota, A média, A quantidade de notas e A situação
    :param nota: Recebe uma quantidade de notas
    :param sit: Situação, se sit for True-Verdadeiro- Mostra a Situação se não situação não sera mostrada
    :return: Retona um dicionario com os valores
    """
    cor = ['\033[1;30m', '\033[1;31m', '\033[1;32m', '\033[1;33m', '\033[1;34m', '\033[1;35m', '\033[1;36m', '\033[1;37m']
    aluno = {}
    med = 0
    aluno['Quantidade de notas'] = len(nota)
    aluno['A maior nota'] = max(nota)
    aluno['A Menor nota'] = min(nota)
    for n in nota:
        med += n
    aluno['A média'] = med / len(nota)
    if sit:
        if med / len(nota) >= 6:
            aluno['Situação'] = 'Boa'
        elif 6 > aluno['A média'] > 3:
            aluno['Situação'] = 'Regular'
        else:
            aluno[f'Situação'] = 'Ruim'
    print(f'{cor[4]}{aluno}')
    for k, v in aluno.items():
        print(f'{cor[6]} {k} é {cor[5]}{v}')


nota(10, 4, 5, 0, sit=True)





print('\033[1;33m')


                                # Resposta do Guanabara


def notas(*n, sit=False):
    """
    -> Função para analisar notas e situação de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma.
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n) / len(n)
    if sit:
        if r['média'] >= 7:
            r['situação'] = 'Boa'
        elif r['média'] >= 5:
            r['situação'] = 'Razoável'
        else:
            r['situação'] = 'Ruim'
    return r


# Programa Principal
resp = notas(5.5, 2.5, 1.5, sit=True)
print(resp)
