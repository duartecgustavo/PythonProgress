# Desafio 55 - Aula 13 : Programa que leia o peso de 5 pessoa e diga qual foi o MAIOR e qual foi o MENOR.

lista=[]
for c in range(1,6):
    num = int(input('Digite um numero: '))
    lista += [num]
print(lista)
print(f'{max(lista)} e {min(lista)}')

# ouuu

'''maior = 0
menor = 0
for c in range(1, 6):
    peso = float(input(f'Me diga o peso da {c}° pessoa: '))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O maior peso é {maior} e o menor peso é o {menor}!')'''


