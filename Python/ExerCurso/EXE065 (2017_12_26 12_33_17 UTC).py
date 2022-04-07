res = 's'
cont = to = Mm = 0
mm = 999
while res == 's':
    n = int(input('\033[1;37m Digite um numero:'))
    cont += 1
    to += n
    if n > Mm:
        Mm = n
    if n < mm:
        mm = n
    res = input('\033[1;35m Quer quontinuar S ou N').strip().lower()[0]
print('\033[1;34m A Média é {} o Maior numero é {} e o Menor é {}'.format(to/cont, Mm, mm))


# Resposta do Guanabara
resp = 's'
soma = quant = media = maior = menor = 0
while resp in 'Ss':
    num = int(input('Digite um número:'))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    res = str(input('Quer continuar? [S/N')).upper().strip()[0]
media = soma / quant
print('você digitou {} numeros e a media foi {}'.format(quant, media))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))
