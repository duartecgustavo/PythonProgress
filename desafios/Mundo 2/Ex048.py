# Desafio 48 - Aula 13 : Apresente a SOMA de todos os NUMEROS IMPARES ENTRE 1 e 500 MULTIPLOS DE 3:

repeticoes = 0
soma = 0

for count in range(1, 501, 2):
    if count % 3 == 0:
        repeticoes = repeticoes+1
        soma = soma+count
        print(soma)
        
print(f'Segundo as condições, numeros IMPARE e MULTIPLOS DE 3 entre 0 e 500 aparecem {repeticoes} e a soma de todos é igual à {soma}!')