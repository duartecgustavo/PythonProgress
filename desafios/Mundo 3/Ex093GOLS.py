# Desafio 93 - Aula 19 : Programa que gerencie o aproveitamento de um jogador de futebol.
# Leia o NOME, quantas PARTIDAS jogou e depois leia quantos GOLS foram feitos em cada partida.
# Guarde tudo em um dicionario e apresente.

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
    
    elif k == 'gols':
        print(f'-'*30)
        print(f'O jogador {banco["Nome"]} fez: ')
        for part, gol in enumerate(gols):
            print(f'=> {part+1}° partida - {gol} gols.')
        print(f'Com o total de {banco["total"]} gols.')

print(f'-'*30)

