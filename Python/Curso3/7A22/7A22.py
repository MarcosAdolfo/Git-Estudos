import uteis                                                # importa um modolo com as funções, uteis e outro codigo que eu criei
                                                            # from ... import...  from e o modolo e import vai ser o nome da função
from pacotets import num                                    # Importando Pacotes

n = int(input('Digite um valor '))
fat = uteis.fatorial(n)
print(f'O fatorial de {n} é {fat}')
print(f'O drobro de {n} é {num.dobro(n)}')
print(f'O triplo de {n} é {num.triplo(n)}')

''' 
Nos Módulos posso criar um outro codigo que contenha as funções que meu codigo nessecita
e importa para meu codigo principal ezemplo posso cria um módulo 'Texto' e neste modulo vaiter
funções para manipular txt ezemplo uma função para titulo outra para roda per com o sem cor para msg para dados etc.

Os pacotes são para quando os Módulos não tenha mais dado conta ai cria um pacote com outros pacoes dentro 
cada pacote responsavel por algo no codigo principal um pacote para numeros outro para txt outro analise de dados etc. 
'''