'''def numero(a, b):
    if a > b:
        maior = a
    else:
        maior = b
    print(maior)

numero(5, 4)'''
from time import sleep


def maior(* num):
    cont = maior = 0
    print('-=' * 30)
    print('Analisando os valores passados... ')
    for valori in num:
        print(f'{valori} ', end='', flush=True)
        sleep(0.3)
        if cont == 0:
            maior = valori
        else:
            if valori > maior:
                maior = valori
        cont += 1
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}')

maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()