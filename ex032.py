"""ano = int(input('Que ano voce quer analisar: '))
if ano % 4 == 0:
    print('BISSEXTO')
else:
    print('NAO É')"""
from datetime import date
ano = int(input('Que ano voce quer analisar: Coloque 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} e BISSEXTO'.format(ano))
else:
    print('O ano {} nao e BISSEXTO'.format(ano))