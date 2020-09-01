# Desafio 100 - Aula 20: Programa que tenha uma lista chamada 'numeros' e duas funções, chamadas sorteio() e somaPar().
# A função sorteio irá sortear 5 numeros e adicionalos dentro da lista.
# E a função somaPar() irá somar os valores pares dentro desta lista.

from random import randint

def sorteio(*num):
    for c in range(0,5):
        numeros.append(randint(0,10))
    print(numeros)

def somaPar(num):
    ssp = 0
    for n in num:
        if n % 2 == 0:
            ssp+=n
    print(ssp)

numeros = []

sorteio(numeros)
somaPar(numeros)