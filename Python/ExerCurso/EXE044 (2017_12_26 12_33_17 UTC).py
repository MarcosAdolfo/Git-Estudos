print('\033[1;35m {:#^40}'.format(' LOJAS PAN '))
preço = float(input('\033[1;36m Preço: '))
print('Como Pretende Paga?')
print('''1 - Á vista no dinheiro/cheque 
2 - Á vista no cartão
3 - Em até 2x no cartão
4 - 3x ou mais no cartão ''')
modo = int(input('Digite o numero referente ao modo de pagamento:'))
if modo == 1:
    dis = preço * 10 / 100
    ou = preço - dis
    print('Voce escoleu paga avista o preço de R${:.2f}, Voce ganhol um desconto de 10% e vai paga so R${:.2f}'.format(preço, ou))
elif modo == 2:
    dis = preço * 5 / 100
    ou = preço - dis
    print('Voce escoleu paga avista no cartão o preço de R${:.2f}, Voce ganhol um desconto de 5% e vai paga so R${:.2f}'.format(preço, ou))
elif modo == 3:
    print('Voce escoleu paga em 2x no cartão o valhol de R${:.2f}, que fica 2x de R${:.2f}'.format(preço, preço / 2))
elif modo == 4:
    aul = preço * 20 / 100
    ou = preço + aul
    pas = int(input('Quantas Parcelas? '))
    parcela = ou / pas
    print('Voce escolheu paga em {}x no cartão o valo de R${:.2f}, Parcelado é {}x de R${:.2f}. Voce vai paga R${:.2f} com o juros'.format(pas, preço, pas, parcela, ou))
else:
    print('\033[1;31m OPÇÃO INVÁLIDA de pagamento. Tente novamente!')

