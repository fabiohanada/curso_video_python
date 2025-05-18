dias = float(input('Quantos dias alugados? '))
km = float(input('Quantos km rodados? '))
diaria = dias * 60
km_rodado = km * 0.15
total = diaria + km_rodado
print('O total a pagar é de R${}' .format(total))