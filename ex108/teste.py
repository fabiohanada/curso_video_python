from ex108 import moeda
#import formatacao

p = float(input('Digite o preco: R$'))
print(f'A metade de R${moeda.moeda(p)}, é R${moeda.moeda(moeda.metade(p))}')
print(f'O dobro de R${moeda.moeda(p)} é R${moeda.moeda(moeda.dobro(p))}')
print(f'Aumentando 10%, temos R${moeda.moeda(moeda.aumentar(p, 10))}')