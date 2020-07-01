# Desafio 78 - Aula 17 : Leia 5 valores adicionando-os em uma lista. Mostre o MAIOR e o MENOR em suas respectivas
# posições

lista = list(int(input(f'Me diga o valor da posição {c+1}: '))for c in range(5))

print('='*40)

print(f'O maior valor digitado foi {max(lista)} e aparece nas posições ',end=' ')
for posicao, maior in enumerate(lista):
    if maior == max(lista):
        print(posicao+1, end='... ')
print(f'\nO menor valor digitado foi {min(lista)} e aparece nas posições ',end=' ')
for posicao, menor in enumerate(lista):
    if menor == min(lista):
        print(posicao+1, end='... ')