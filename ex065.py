'''cont = 0
soma = 0
maior = 0
menor = 99
while cont != 999:
    n = int(input("Digite um numero: "))
    parada = str(input('Deseja continuar? [S/N] '))
    cont += 1
    soma += n
    if n > maior:
        maior = n
    if n < menor:
        menor = n
    if parada == 'n':
        media = soma / cont
        print('Voce digitou {} numeros e a media foi de {:.2f}'.format(cont, media))
        print(maior)
        print(menor)
        break'''


resp = 'S'
soma = quant = media = maior = menor = 0
while resp in 'Ss':
    num = int(input('Digite um numero: '))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Quer continuar? [S/N} ')).upper().strip()[0]
media = soma / quant
print('Voce digitou {} numeros e a media foi {}'.format(quant, media))
print('O maior foi {} e o menor foi {}'.format(maior, menor))






