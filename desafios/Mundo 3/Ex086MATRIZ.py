# Desafio 86 - Aula 18 : Crie uma MATRIZ de dimensão 3x3 e preencha com valores do teclado.
# No final mostre na tela com a formatação correta.
# minha versão

pos1 = pos2 = 0
count = 0
posic = []
lista = []

for c in range(1,10):
    posic.append(int(input(f'Diga um valor para posição [{pos2}, {pos1}]:')))
    pos1 += 1
    if pos1 > 2:
        pos1=0
        pos2+=1

    lista.append(posic[:])
    posic.clear()

print('-='*15)

for valor in lista:
    print(f'{valor}',end=' ')
    count += 1
    if count > 2:
        print()
        count = 0