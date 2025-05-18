prod = float(input('Qual é o preco do produto? '))
desconto = prod * 0.05
custo = prod - desconto

print('O produto que custava R${}, na promocao de 5%, vai custar R${}'.format(prod, custo) )