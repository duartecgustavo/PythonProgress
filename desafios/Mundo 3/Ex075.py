# Desafio 75 - Aula 16 : Leia 4 valores e armazene-os em uma TUPLA:
# A/ Quantas vezes aparece o numero 9?
# B/ Em que posiição foi digitado o primeiro valor 3?
# C/ Quais foram os numeros PARES?

tupla = tuple(int(input('Me diga um numero:')) for i in range(4))

if 9 in tupla:
    repet = tupla.count(9)
    print(f'\nA : O numero "9" aparece {repet}x.')
else: print('\nNão foi digitado nenhum 9.')

if 3 in tupla:
    pos = tupla.index(3)
    print(f'\nO valor "3" aparece pela primeira vez na posição {pos+1}.')
else: print('\nO numero 3 não foi digitado nenhuma vez.')

print('\nOs valores pares são: ',end=' ')

for numero in tupla:
    if numero % 2 == 0: # analizando se é par
        print(numero,end=' ')
