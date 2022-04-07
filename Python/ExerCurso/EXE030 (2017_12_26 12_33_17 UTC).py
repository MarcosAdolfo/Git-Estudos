n = int(input('\033[1;34m Um numero '))
n1 = n % 2
if n1 == 0:
    print('\033[1;32;40m Este numero {} é par'.format(n))
else:
    print('\033[1;33;40m O numero {} é impar'.format(n))
