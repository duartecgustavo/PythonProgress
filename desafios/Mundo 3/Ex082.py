# Desafio 82 - Aula 17 : Programa que leia varios numeros e add a uma lista.
# Crie duas listas extras que vão conter valores pares e valores impares respectivamente.
# Ao final mostre as 3 listas.

listamain = listapar = listaimpar = list()

while True:
    valor = int(input('Diga um numero: '))

    if valor in listamain:
        while valor in listamain:
            valor = int(input(f'O numero {valor} já existe na lista.\nDiga um novo numero: '))
    else:
        listamain.append(valor)

    choice = str(input('Quer continuar?[S/N] ')).upper()[0]
    while choice not in 'SN':
        choice = str(input('Opção invalida!\nQuer continuar?[S/N] ')).upper()[0]
    if choice in 'N':
        break

print(listamain)

for num in listamain:
    if num % 2 == 0:
        listapar.append(num)
    elif num % 2 == 1:
        listaimpar.append(num)

print(f'Os valores pares digitados são:\n{listapar}')
print(f'Os valores impares digitados foram:\n{listaimpar}')