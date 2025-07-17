'''def ficha():
    if isinstance(nome, str):
        return print(f'O jogador {nome} fez {gols}(s) no campeonato')
    else:
        return  print('Desconhecido')


nome = (input('Nome do jogador:'))
gols = (input('Numero de gols:'))
ficha()'''

def ficha(jog='<desconhecido>', gol=0):
    print(f'O jogador {jog} fez {gol}(s) no campeonato.')

# programa principal
n = str(input('Nome do jogador: '))
g = str(input('Numero de gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gol=g)
else:
    ficha(n, g)