# Desafio 79 - Aula 17 : Programa que leia numeros e cadastre-os em uma lista.
# Caso o numero seja repetido ele não sera cadastrado.
# No final mostre a lista em ordem crescente.

lista = []
numero = 0

while True:
    numero = int(input('Diga um numero: '))

    if numero in lista:
        print('Este numero já existe na lista')
    else:
        print('Numero adicionado com sucesso..')
        lista.append(numero)

    choice = str(input('\nDeseja continuar?[S/N] ')).lower()[0]
    while choice not in 'sn':
        choice = str(input('Opção invalida!\nDeseja continuar?[S/N] ')).lower()[0]
    if choice in 'n':
        break

print(sorted(lista))