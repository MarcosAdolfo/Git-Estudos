time = ('Palmeiras', 'Internacional', 'Flamengo', 'São Paulo', 'Grêmio', 'Atlético-MG', 'Santos',
        'Cruzeiro', 'Atlético-PR', 'Fluminense', 'Bahia', 'Corinthians', 'Vasco', 'Botafogo',
        'Ceará', 'Vitória', 'América-MG', 'Chapecoense', 'Sport', 'Paraná Clube')
for ps, ch in enumerate(time):
    if ch == 'Chapecoense':
        poch = ps
print('\033[1;36m Lista de times do Brasileirão', time)
print(f'\033[1;38m Times em ordem alfabética: {sorted(time)}')
print(f'\033[1;35m Os cinco primeiros são: {time[0:5]}')
print(f'\033[1;33m Os útimos 4 quolocados são: {time[-4:]}')
print(f'\033[1;34m A {time[poch]} esta na {poch + 1}° posição')






                                        # Resposta do Guanabara

times = ('Palmeiras', 'Internacional', 'Flamengo', 'São Paulo', 'Grêmio', 'Atlético-MG', 'Santos',
        'Cruzeiro', 'Atlético-PR', 'Fluminense', 'Bahia', 'Corinthians', 'Vasco', 'Botafogo',
        'Ceará', 'Vitória', 'América-MG', 'Chapecoense', 'Sport', 'Paraná Clube')
print('-=' * 15)
print(f'\033[1;37mLista de times do Brasileirão: {times}')
print('-=' * 15)
print(f'Os 5 primeiros são {times[0:5]}')
print('-=' * 15)
print(f'Os 4 útimos são {times[-4:]}')
print('-=' * 15)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-=' * 15)
print(f'O chapecoense está na {times.index("Chapecoense")+1}ª posição')
print('-=' * 15)
