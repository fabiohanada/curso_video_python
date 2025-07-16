'''def lin():
    print('-' * 30)

lin()
print('  CURSO EM VIDEO  ')
lin()
print('  PYTHON  ')
lin()
print('  VIDEO  ')
lin()

def titulo(txt):
    print('-' * 30)
    print(txt)
    print('-' * 30)


titulo('  CURSO EM VIDEO  ')
titulo('  PYTHON  ')
titulo('  VIDEO  ')

def soma(a, b):
    s = a + b
    print(s)

soma(2, 3)
def contador(* num):
    for valor in num:
        print(f'{valor} ', end='')
    print('FIM')

contador(2, 1, 7)
contador(8, 0)
def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1

valores = [6, 3, 9, 1, 0, 2]
print(valores)
dobra(valores)
print(valores)'''

def soma(* valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')

soma(5, 2)
soma(2, 9, 4)












