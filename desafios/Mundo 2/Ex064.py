# Desafio 64 - Aula 14 : Programa que leia varios numeros inteiros e a condição de parada é '999'.
# No final mostre QUANTOS NUMEROS foram digitados e a SOMA entre eles:

num = 0
count = 0
soma = 0
c = 0

while num != 999:
    soma += c
    c = int(input('Numero[999 para parar]   : '))
    count += 1
    num = c
    if c == 999:
        count -= 1
print(f'A soma de todos os {count} valores digitados é igual à {soma}.')