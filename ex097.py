'''def escreva(txt):
    print('-' * 30)
    print(txt)
    print('-' * 30)

escreva('Fabio')
escreva('Curso')
escreva('Puthon')'''


def escreva(msg):
    tam = len(msg) + 4
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)

escreva('Fabio')
escreva('Curso')