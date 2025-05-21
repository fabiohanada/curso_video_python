print('=========LOJAS APP=========')
compra = float(input('Preço das compras: R$ '))
print('FORMAS DE PAGAMENTO')
print('[ 1 ] a vista dinheiro')
print('[ 2 ] a vista no cartao')
print('[ 3 ] 2x no cartao')
print('[ 4 ] 3x ou mais no cartao')
formas = int(input('Qual e a opcao? '))
if formas == 1:
    desconto = compra - (compra * 10/100)
    print('Sua compra a vista no dinheiro sera de R$ {:.2f} com 10% de desconto'.format(desconto))
elif formas == 2:
    desconto2 = compra - (compra * 5/100)
    print('Sua compra a vista no cartao sera de R$ {:.2f} com 5% de desconto'.format(desconto2))
elif formas == 3:
    print('Sua compra em duas vezes no cartao sera de R$ {:.2f} sem desconto'.format(compra))
elif formas == 4:
    parcelas = int(input('Quantas parcelas: '))
    compra_juros = compra + (compra * 20/100)
    parcela_juros = compra_juros / parcelas
    print('Sua compra sera parcelada em {}x de R$ {:.2f} com JUROS'.format(parcelas, parcela_juros))
    print('Sua compra de R$ {:.2f} vai custar R$ {:.2f} no final.'.format(compra, compra_juros))
else:
    print('Opcao invalida, tente novamente')