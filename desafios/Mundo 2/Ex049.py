# Desafio 49 - Aula 13 : TABUADA com LAÇO.

a = int(input('Digite o numero que deseja da tabuada: '))

print(f'A tabuada de {a} é:')

for tabu in range (1,11):
          print(f'{a} x {tabu} = {a*tabu}')