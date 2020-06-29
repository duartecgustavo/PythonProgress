# Desafio 50 - Aula 13 : Leia 6 NUMEROS INTEIROS e mostre a SOMA apenas daqueles que forem PARES.

soma = 0
conta = 0

for nume in range(0, 6):
    numero = int(input('Digite um numero: '))
    if numero % 2 ==0:
        soma = soma + numero
        conta = conta + 1

print(f'Dos numeros que você digitou, apenas {conta} são pares e destes numeros a soma é igual à {soma}!')