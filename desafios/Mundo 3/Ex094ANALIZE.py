# Desafio 94 - Aula 19 : Programa que leia NOME, SEXO e IDADE de varias pessoas, guarde cada dado em um dicionario e ao fim mostre:
# A/ Quantas pessoas foram cadastradas.
# B/ Média de idade do grupo.
# C/ Lista com todas as mulheres.
# D/ Lista com todas as pessoas com IDADE acimada média.

from math import trunc

lista =[]
banco =  {}
choice = ''
soma = countmulher = countvelhos = 0

while True: 

    banco['nome'] = str(input('Seu nome: ').capitalize())

    sexo = str(input('Seu sexo: [H/M] ').upper()[0])
    while sexo not in 'HM':
        print('=-'*15)
        sexo = str(input('Opção invalida!\nSeu sexo: [H/M] ').upper()[0])
    if sexo in 'M':
        countmulher +=1
    banco['sexo'] = sexo

    banco['idade'] = int(input('Sua idade: '))
    lista.append(banco.copy())
    soma += banco['idade']

    choice = str(input('Quer continuar? [S/N]')).upper()[0]
    print('=-'*15)
    while choice not in 'SN':
        choice = str(input('Opção invalida!\nQuer continuar? [S/N]')).upper()[0]
        print('=-'*15)
    if choice in 'N':
        break

media = soma/len(lista)

print('=-'*15)
print(lista)
print('=-'*15)

print(f'    ==> Foram cadastradas {len(lista)} pessoas!\n')

print(f'    ==> A média da idade da galera é de {trunc(media)} anos.\n')

if countmulher > 0:
    print(f'    ==> As mulheres cadastradas foram: ',end='')
    for pos, cad in enumerate(lista):
        if cad['sexo'] in 'M':
            print(cad['nome'], end=' ')
else:
    print('     ==> Não foram registradas mulheres.')
print('\n')

print('    ===> As pessoas acima da média de idade são: \n')
for cad in lista:
    if cad['idade'] > media:
        for indice, valor in cad.items():
            print(f'{indice} = {valor};', end=' ')
        print('')
