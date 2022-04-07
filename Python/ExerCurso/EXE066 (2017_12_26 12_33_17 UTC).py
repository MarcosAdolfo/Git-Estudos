res = cont = 0
while True:
    n = int(input('\033[1;34m Digite um numero [999 para sai]'))
    if n == 999:
        break
    cont += 1
    res += n
print(f'\033[1;37m Foi digitados {cont} números e a soma é {res}')
