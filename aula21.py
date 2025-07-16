'''def contador(i, f, p):

    -> Faz uma contagem e mostra na tela
    :param i: inicio da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno

    c = i
    while c <= f:
        print(f'{c} ', end='')
        c += p
    print('FIM!')

contador(2, 10, 2)
help(contador)

def somar(a, b, c=0):
    s = a + b + c
    print(s)

somar(2, 4)'''

def somar(a, b, c,):
    s = a + b + c
    return s

r1 = somar(3, 2, 5)
print(r1)