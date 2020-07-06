# Desafio 80 - Aula 17 : Programa que faça a mesma coisa que o desafio 79. No entando...
# O programa devera ordenar os numeros sem o comando 'sorted' e devera mostrar a posição que o numero foi adicionado.

lista = []
count = 0

while True:
    num = int(input('Diga um numero: '))
    count += 1

    if num not in lista:
        if count == 1 or num > max(lista):
            lista.append(num)
            print(f'O numero {num} foi add a ultima posição da lista.')
        else:
            pos = 0
            while pos < len(lista):
                if num <= lista[pos]:
                    lista.insert(pos,num)
                    print(f'O numero {num} foi add a posição {pos} da lista.')
                    break
                pos+=1
    else:
        print('Este numero já esta na lista.')

    choice = str(input('Deseja continuar?[S/N] ')).upper()[0]
    while choice not in 'SN':
        choice = str(input('Opção invalida!\nDeseja continuar?[S/N] ')).upper()[0]
    if choice in 'N':
        break

print(lista)