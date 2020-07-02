# Desafio 73 - Aula 16 : Crie uma TUPLA com os 20 primeiros colocados da tabela do Brasileirão, depois mostre:
# A - Os 5 primeiros colocados
# B - Os quatro ultimos colocados
# C - Lista em ordem alfabetica
# D - Em que posição na tabela está o time do SANTOS?

times = ('Gremio', 'Corinthians','Internacional','santos','Palmeiras','Flamengo','São Paulo','Vasco','Fluminense','Atlético','Bahia','Coritiba','Goias','Sport','Botafogo','Chapecoense','Ceara','Bragantino','Avaí','Cruzeiro')

print('-='*25)
print(f'{"ANALIZE DE TIMES BRASILEIRÃO 2020": ^50}')
print('-='*25)

for t in times:
    print(f'{times.index(t)+1}° - {t}')


print(f'\nOs 5 primeiros colocados da série A do Brasileirão são \n{times[:5]}')

print(f'\nOs quatro ultimos times da tabela são \n{times[-1:-5:-1]}')

print(f'\nA lista de times em ordem alfabética é \n{sorted(times)}')

for c in range(0, len(times)):
    if 'santos' in times[c]:
        print(f'\nO santos aparece na {c+1}° posição da tabela!')
# print(f'O santos aparece na {times.index("santos")+1}')
