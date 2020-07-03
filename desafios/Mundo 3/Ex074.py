# Desafio 74 - Aula 16 : Programa que deve gerar 5 numeros aleatórios e adicionalos a uma TUPLA.
# Depois disso mostre a listagem dos numeros gerados e indique qual é o MAIOR e qual é o MENOR.

from random import randint

tupla = ((randint(1,10)),(randint(1,10)),(randint(1,10)),(randint(1,10)),(randint(1,10)))

for n in tupla:
    print(n, end=' ')
print(f'\nO maior valor da tupla é {max(tupla)} e o menor é {min(tupla)}.')
