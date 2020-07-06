# Desafio 81 - Aula 17 : Programa que leia numeros pelo teclado:
# A/ Quantos numeros foram digitados?
# B/ A lista de valores ordenada de forma decrecente.
# C/ Se o valor 5 foi digitado ou não na lista.

count = 0
lista = []

while True:
    lista.append(int(input('Diga um numero: ')))

    count+=1

    choice = str(input('Quer continuar?[S/N] ')).upper()[0]
    while choice not in 'SN':
        choice = str(input('Opção invalida!\nQuer continuar?[S/N] ')).upper()[0]
    if choice in 'N':
        break

copialista = lista[:]
lista.sort()

print(f'A/ Foram digitados {count} numeros.')
# ouu print(f'Você digitou {len(lista)} numeros.')

print(f'B/ A lista de numeros em ordem decrescente é:\n{lista[::-1]}', end=' ')
# ouu print(f'Os valores em ordem decrescente são {sorted(lista, reverse = True)}')

if 5 in lista:
    for pos, content in enumerate(copialista):
        if content == 5:
            print(f'\nC/ O numero 5 aparece na lista na {pos+1}° posição.')
else:
    print(f'\nC/ O 5 não aparece na lista.')

# ouu print('O número 5 aparece na lista!' if 5 in lista else 'o número 5 não aparece na lista!')p