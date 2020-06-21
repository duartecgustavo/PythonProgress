# Desafio 48 - Aula 13 : Programa que apresente a SOMA de todos os NUMEROS IMPARES ENTRE 1, 500 MULTIPLOS DE 3:

n = 0
m = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        n = n+1
        m = m+c
        print(m)
print(f'Segundo as condições, numeros IMPARES, MULTIPLOS DE 3 entre 0, 500 aparecem {n} e a soma de todos é igual à {m}!')