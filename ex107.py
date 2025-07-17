from uteis import numero

preco = int(input('Digite o preço: '))
print(f'A metade de R${preco} é R${numero.metade(preco)}')
print(f'O dobro de R${preco} é R${numero.dobro(preco)}')
print(f'Aumentando 10%, temos R${numero.aumento(preco)}')