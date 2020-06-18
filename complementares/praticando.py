# Desafio 65 - Aula 14 : Programa que leia varios numeros, no final da execução mostre:
# À MÉDIA entre os numeros / Qual é o maior e o menor.
count = maior = menor = pluss = 0

while True:
    num = int(input('Me diga um numero: '))

    count+=1
    pluss +=num

    if count == 1:
        maior = num
        menor = num
    else:
        if num < menor:
            menor = num
        elif num > maior:
            mior = num



    choice = str(input('Quer continuar?[S/N] ')).upper()[0]
    while choice not in 'SN':
        choice = str(input('\033[31mOpção invalida!\033[m\nQuer continuar?[S/N] ')).upper()[0]

    if choice in 'N':
        break
    print('-='*15)

print(pluss, count)
print(f'A média é {pluss/count}')
print(f'Menor {menor} / Maior {maior}')
