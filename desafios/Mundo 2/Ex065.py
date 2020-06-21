# Desafio 65 - Aula 14 : Programa que leia varios numeros, no final da execução mostre a, MÉDIA entre todos os numeros e qual foi o maior e o menor.

choise = ''
soma = maior = menor = count = 0
while not 'N' in choise:
    num = int(input('Numero: '))
    choise = str(input('Quer continuar? ')).upper()
    count+=1
    soma += num
    if count == 1:
        maior = num
        menor = num
    if num > maior:
        maior = num
    if num < menor:
        menor = num
media = soma/count
print(f'A media de todos os {count} valores digitados é {media}!\nO maior numero é {maior} e o menor é {menor}!')