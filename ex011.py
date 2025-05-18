largura = float(input('Largura da parede:'))
altura = float(input('Altura da parede: '))
dim = largura * altura
tinta = dim * 0.5
print('Sua parade tem a dimensão de {}x{} e a sua area é de {}m2'.format(largura, altura, dim))
print('Para pintar a sua parede, voce precisara de {}l de tinta'.format(tinta))
