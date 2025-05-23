from datetime import date
ano_atual = date.today().year
totmaior = 0
totmenor = 0
for pess in range(1, 8):
    ano = int(input('Em que a {}a pessoa nasceu? '.format(pess)))
    idade = ano_atual - ano
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print('Ao todo tivemos {} pessoas maiores de idade.'.format(totmaior))
print('E tambem tivemos {} pessoas menores de idade.'.format(totmenor))
