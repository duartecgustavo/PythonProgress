# Desafio 54 - Aula 13 : Programa que leia o ano de nascimento de 7 pessoas e diga quantas sao maiores de idade e quantas não:

from datetime import date
cont = 0
cont1 = 0
anotual = date.today().year
for c in range (1, 8):
    ano = int(input(f'Em que ano à {c}° nasceu? '))
    if (anotual-ano) >=  19:
        cont += 1
    else:
        cont1 += 1
print(f'O numero de pessoas maiores de idade é {cont} e menores é {cont1}!')

