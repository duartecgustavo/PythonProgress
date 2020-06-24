# Desafio 09 - Aula 07 : Tabuada!

print('-='*25)
print(f'{"-> TABUADA <-":^50}')
print('-='*25)

nome = input('\033[33mOlá, digite seu nome aqui\033[m: ').strip()

numero = int(input('Digite um numero: '))

print(f'\033[34m{nome}\033[m, a \033[31mtabuada\033[m de \033[31m{numero}\033[m é igual:\n\033[32m{numero}x0 = {numero*0}\n{numero}x1 = {numero*1}\n{numero}x2 = {numero*2}\n{numero}x3 = {numero*3}\n{numero}x4 = {numero*4}\n{numero}x5 = {numero*5}\n{numero}x6 = {numero*6}\n{numero}x7 = {numero*7}\n{numero}x8 = {numero*8}\n{numero}x9 = {numero*9}\n{numero}x10 = {numero*10}')