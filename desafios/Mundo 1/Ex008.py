# Desafio 8 - Aula 7 : Escreva um programa que leia um valor em metros e traga o resultado em CM e em MM.

nome = input('\033[31mOlá, digite seu nome ao lado\033[m: ')

n1 = int(input('Agora digite a \033[31mdistancia\033[m em \033[33mmetrô\033[m do seu quarto até a porta de sua casa: '))

print(f'\033[31m{nome}\033[m, a mesma \033[31mdistancia\033[m corresponde em: \n \033[31m{n1 * 0.001:.3f}km \n \033[32m{1 * 0.01}hm \n \033[33m{n1 * 0.1}dam \n \033[34m{n1 * 10}dm \n \033[35m{n1*100}cm \n \033[36m{n1*1000}mm')
