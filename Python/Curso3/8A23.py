# Tente alguma coisa
try:            # Vai tentar rodar o codigo e vai ver ser tem ou não algum erro
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
# Se Falha
except (ValueError, TypeError): # except com tipos de erros
    print('Tivemos um problema com os tipos de dados que você Digitou.')    # msg personalizada do erro
except ZeroDivisionError:   # Tipos de erro de divisão por zero
    print('Não é possivel dividir um úmero por zero!')
except KeyboardInterrupt:
    print('O usuario preferiu não informar os dados!')
except Exception as erro:
    print(f'Problema econtrado foi {erro.__class__}')  # vai mostra a Class do erro
# se deu certo
else:           # Ser não o coreu nem um erro ele vai acotecer
    print(f'O resutado é {r:.1f}')
# Finamente
finally:       # Vai acontecer independente ser deu certo ou falho
    print('Volte sempre! Muito obrigado!')  # Vai mostra no fim sempre independente ser deu certo ou não
