times = ('Flamengo', 'Cruzeiro', 'Bragantino', 'Palmeiras', 'Fluminense', 'Botafogo', 'Bahia',
         'Mirassol', 'Atletico-MG', 'Ceara', 'Corinthians', 'Gremio', 'Sao Paulo', 'Inter',
         'Vasco', 'Fortaleza', 'Santos', 'Juventude', 'Sport')
print('-=' * 30)
print(f'Lista de times do Brasileirao {times}')
print('-=' * 30)
print(f'Os 5  primeiros são {times[0:5]}')
print('-=' * 30)
print(f'Os 4 ultimos são {times[-4:]}')
print('-=' * 30)
print(sorted(times))
print('-=' * 30)
print(f'O {times[7]} esta na {times.index("Mirassol")+1} posição')
