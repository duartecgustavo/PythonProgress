# Desafio 30 - Aula 10 : Programa que leia um numero e me diga se ele é para ou impar.

numero = int(input('Digite um numero inteiro: '))
if (numero % 2) == 1:
    print(f'O numero \033[32m{numero}\033[m é \033[34mimpar\033[m!')
else:
    print(f'O numero \033[32m{numero}\033[m é \033[31mpar\033[m')