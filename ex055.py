maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input('Peso da {}a pessoa: '.format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(maior)
print(menor)