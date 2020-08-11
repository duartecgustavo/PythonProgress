# Desafio 93 - Aula 19 : Programa que gerencie o aproveitamento de um jogador de Futebol.
# Leia o NOME e quantas PARTIDAS o jogador jogou e depois leia quantos GOLS foram feitos em cada partida.
# Guarde tudo em um dicionario e apresente!

banco = {}
gols = []
total = 0

banco['Nome'] = str(input('Nome do Jogador: ').capitalize())

partidas = int(input('Partidas disputadas: '))
banco['Partidas'] = partidas

print(f'{"GOLS":-^30}')
for count in range(0, partidas):
    gols.append(int(input(f'{count+1}° partida - ')))
    total += gols[count]
print(f'-'*30)
banco['gols'] = gols.copy()
banco['total'] = total

print(banco)

for k, v in banco.items():

    if k == 'Nome':
        print(f'Nome do jogador: {v} ')

    elif k == 'Partidas':
        print(f'Partidas Disputadas: {v} jogos')
    
    elif k == 'total':
        print(f'Total Gols marcados: {v}')

print(f'-'*30)