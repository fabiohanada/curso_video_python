cont = 0
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
        break



