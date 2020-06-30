# Desafio 52 - Aula 13 : Programa que leia um numero e diga se é um numero PRIMO.

conta = 0

primo = int(input('Me diga um numero: '))

for c in range(1, primo+1):
    if primo % c == 0 :
        print('\033[34m', end='')
        conta += 1
    else:
        print('\033[m', end='')
    print(f'{c}', end=' ')
    
if conta == 2:
    print(f'\n\033[mO numero {primo} é primo!')
else:
    print(f'\n\033[mO numero {primo} não é primo!')