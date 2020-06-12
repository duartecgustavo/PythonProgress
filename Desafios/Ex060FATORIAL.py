# Desafio 60 - Aula 14 : Programa que leia um numero e mostre seu fatorial.

num1 = int(input('Um numero: '))
count = num1
f = 1
print(f'Calculando {num1}!', end=' ')
while count > 0:
    print(f'{count}', end='')
    print(' x ' if count > 1 else ' = ', end='')
    f = f * count
    count -= 1
print(f'{f}')

# ouuu

''' MÉTODO COM BILBIOTECA MATH
from math impor factorial
n = int(input('Digite um numero: '))
fatorial = factorial(n)
print(f'O fatorial de {n} é {fatorial}.')'''