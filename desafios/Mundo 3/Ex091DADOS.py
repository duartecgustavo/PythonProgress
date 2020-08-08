# Desafio 91 - Aula 19 : Programa onde 4 jogadores joguem dados e cada um receba um valor aleatorio (1, 6).
# Guarde esses valores em um dicionario e depois apresente os resultados em ORDEM.
# Mostre o o vencedor que tirou o maior numero.

from random import randint
from time import sleep

dado = {}
valores = []
count = count2  =  0
ranking = []
maiorjog = maiordado = 0

dado['jogador_1'] = randint(1,6)
dado['jogador_2'] = randint(1,6)
dado['jogador_3'] = randint(1,6)
dado['jogador_4'] = randint(1,6)

valores.append(dado.copy())

print('Valores Sorteados: ')
for jogador in valores:
    count+=1
    for indice, jog in jogador.items():
        print(f'    O {indice} tirou {jog}.')
        sleep(0.35)

print('=-'*15)
print('Ranking dos jogadores: ')

count=0
for jogador in valores:
    while len(jogador) != 0:
        for indice, dados in jogador.items():
            if count == 0 or dados >= maiordado:
                maiordado=dados
                maiorjog=indice
            count+=1
        count=0
        count2+=1
        sleep(0.35)
        print(f'    {count2}° lugar : {maiorjog} que tirou {maiordado}.' )

        del jogador[f'{maiorjog}']

