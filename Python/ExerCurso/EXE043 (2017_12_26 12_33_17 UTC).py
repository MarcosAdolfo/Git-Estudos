peso = float(input('\033[1;35m Seu peso Kg: '))
altura = float(input('Sua altura m:' ))
imc = peso / (altura ** 2)
print('\033[1;33;47m Seu Peso é {}Km e sua altura é {}m è seu IMC ede {:.1f}'.format(peso, altura, imc))
if imc < 18.5:
    print('\033[1;33m Abaixo do Peso')
elif  18.5 <= imc < 25:
    print('\033[1;32m Peso Ideal')
elif imc >= 25 and imc <=30:
    print('\033[1;36m Sobrepeso')
elif imc >= 30 and imc <= 40:
    print('\033[1;34m Obesidade')
else:
    print('\033[1;31m Obesidade mórbida')
