# Desafio 100 - Aula 20: Programa que tenha uma lista chamada numeros[] e duas funções chamadas sorteio() e somaPar().
# A função sorteio() irá sortear 5 numeros e adicionalos dentro da lista numeros[].
# E a função somaPar() irá somar os valores pares dentro desta lista.

from random import randint

lista = [0, 0, 0, 0, 0]

def sorteio(lst):
    print('Sorteando os 5 valores da lista:', end=' ')
    for count in range(0,5):
        lst[count] = randint(0,10)
    print(lst, 'PRONTO!')

def somaPar(lst):
    soma=0
    print(f'Somando os valores pares de {lista}, temos',end=' ')
    for valor in lst:
        if valor % 2 ==0:
            soma += valor
    print(soma)

sorteio(lista)
somaPar(lista)