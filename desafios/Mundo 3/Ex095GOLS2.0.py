# Desafio 95  - Aula 19 : Melhorar código do desafio 93.
# Programa que gerencie o aproveitamento de varios jogadores de Futebol.
# Leia o NOME e quantas PARTIDAS o jogador ou jogadores jogaram e depois leia quantos GOLS foram feitos em cada partida.
# Apresente uma tabela dinamica  onde eu possa consultar os detalhes de cada jogador.

jogador = {}
time = []
gols = []
total = count = 0

#------------------------------------------------ LEITURA DOS DADOS ------------------------------------------------#

while True:

    jogador['nome'] = str(input('Nome do Jogador: ').capitalize())

    partidas = int(input('Partidas disputadas : '))
    jogador['partidas'] = partidas

    print(f'{" GOLS ":-^30}')
    for count in range(0, partidas):
        gols.append(int(input(f'{count+1}° partida: ')))
        total += gols[count]
    jogador['gols'] = gols[:]
    jogador['total'] = total
    gols.clear()
    total = 0

    time.append(jogador.copy())

    print('-'*30)
    choice = str(input('Deseja continuar? [S/N] ').upper()[0])
    print('-'*30)
    while choice not in 'SN':
        choice = str(input('Opção invalida!\nDeseja continuar? [S/N] ').upper()[0])
    if choice in 'N':
        break


#------------------------------------------------ AMOSTRAGEM DOS DADOS ------------------------------------------------#
print(time)

print(f'{"Cod.":<5}{"Jogador.":<15}{"Gols.":<15}{"Total.":<15}')
for pos, jogador in enumerate(time):
    print(f'{pos:<5}',end='')
    for ind, valor in jogador.items():
        if ind in 'nome' or ind in 'gols' or ind in 'total':
            print(f'{str(valor):<15}',end='')
    print('')

#------------------------------------------------ ANALIZE DOS DADOS ------------------------------------------------#

choice = str(input('Quer analizar um jogador em especifico? [S/N]')).upper()[0]
while choice not in 'SN':
    choice = str(input('Opção invalida!\nDeseja continuar? [S/N] ')).upper()[0]

while choice in 'S':
    print('-'*40)
    analise = int(input('Código do jogador para analise: '))
    while analise >= len(time):
        print('-'*40)
        analise = int(input(f'Opção invalida!\nCódigo correto do jogador para analise: '))
        
    for pos, jogador in enumerate(time):
        if analise == pos:
            print('-'*40)
            print(f'- LEVANTAMENTO DO JOGADOR {jogador["nome"]}')
            for pos, valor in enumerate(jogador["gols"]):
                print(f'    {pos+1}° jogo: {valor}')
                count+=1

    count = 0
    print('-'*40)
    choice = str(input('Quer analizar outro jogador em especifico? [S/N]')).upper()[0]
    while choice not in 'SN':
        print('-'*40)
        choice = str(input('Opção invalida!\nDeseja continuar? [S/N] ')).upper()[0]

print('='*30)
print('Programa finalizado!')

