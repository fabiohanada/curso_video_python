from ex109 import moeda
#import formatacao

p = float(input('Digite o preco: R$'))
print(f'A metade de {moeda.moeda(p)}, é {moeda.metade(p, True)}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.dobro(p, True)}')
print(f'Aumentando 10%, temos {moeda.aumentar(p, 10, True)}')
print(f'Reduzindo 13%, temos {moeda.diminuir(p, 13, True)}')