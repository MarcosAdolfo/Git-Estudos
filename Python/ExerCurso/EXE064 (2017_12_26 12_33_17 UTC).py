n = cont = rs = s = 0
while n < 999:
    cont += 1
    rs = s
    n = int(input('\033[1;36m Digite um numero (999 para para): '))
    n += s
    s = n
print('\033[1;35mVocê digitou {} Números é a soma é \033[1;36m{}'.format(cont - 1, rs))
print('\033[1;33mFim')


# Resposta do Guanabara

num = cont = soma = 0
num = int(input('Digite um número [999 para parar]'))
while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite um número [999 para parar]'))
print('Você digitou {} números e a soma entre eles foi {}.'.format(cont, soma))
