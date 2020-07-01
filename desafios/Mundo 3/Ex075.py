# Desafio 75 - Aula 16 : Programa que leia 4 valores pelo teclado e armazene-os em uma TUPLA;
# A/  Quantas vezes aparece o numero 9
# B/ Em que posiição foi digitado o primeiro valor 3
# C/Quais foram os numeros PARES

tupla = tuple(int(input('Me diga um numero:')) for i in range(4))

if 9 in tupla:
    a = tupla.count(9)
    print(f'\nA : O numero "9" aparece {a}x.')
else: print('\nNão foi digitado nenhum 9.')

if 3 in tupla:
    b = tupla.index(3)
    print(f'\nO valor "3" aparece pela primeira vez na posição {b+1}.')
else: print('\nO numero 3 não foi digitado nenhuma vez.')

print('\nOs valores pares são: ',end=' ')

for c in tupla:
    if c % 2 == 0:
        print(c,end=' ')
