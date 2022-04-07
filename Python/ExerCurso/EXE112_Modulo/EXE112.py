from ExerCurso.EXE112_Modulo.utilidadescev import moeda, dados

numero = str(input('\033[1;36mDigite o preço: R$'))
moeda.Resumo(numero, 10, 5)


print('\033[1;35m')

                                # Resposta do Guanabara

p = dados.LeiaDinheiro('\033[0;35mDigite o preço: R$')
moeda.Res(p)
