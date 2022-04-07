# 1modo

sd = str(input('\033[1;32;45m Sua cidade é? ')).strip().lower()
sd1 = sd.split()
santos = 'santos'
if sd1[0] == santos:
    print('\033[1;32;45m Voce é de Santos')
else:
    print('\033[1;33;45m Voce não é de Santos')

 # 2modo
print('\033[1;35;42m', sd[:6] == santos)
