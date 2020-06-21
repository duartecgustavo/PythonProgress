# Desafio 32 - Aula 10 : Um programa que leia um ano e diga se ele é bizssexto ou não.

import time # Biblioteca tempo
from datetime import date # Data de hoje
ano = int(input('Qual o ano que você deseja saber se é \033[4mBISSEXTO\033[m ou coloque \033[31m0 para analisar o ano atual\033[m: '))
print('\033[31mloading...\033[m')
time.sleep(2)

if ano == 0:
    ano = date.today().year # Vai buscar a data de hoje e com o comando .year apenas o ano
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0: #FORMULA DO BISSEXTO
    print(f'O ano \033[34m{ano} é BISSEXTO\033[m!')
    
else:
    print(f'O ano \033[31m{ano} não é BISSEXTO\033[m!')