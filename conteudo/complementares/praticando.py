# Desafio 94 - Aula 19 : Programa que leia NOME, SEXO e IDADE de varias pessoas, guarde cada dado em um dicionario e ao fim mostre:
# A/ Quantas pessoas foram cadastradas.
# B/ Média de idade do grupo.
# C/ Lista com todas as mulheres.
# D/ Lista com todas as pessoas com IDADE acima da média.

def escolha(X):
    while X not in 'SN':
        choice = str(input('Opção invalida!\nDeseja continuar? [S/N] ').upper()[0])   


def linha():
    print('-='*15)

pessoa = dict()
galera = list()
somaidade = 0

while True:
    pessoa['nome'] = str(input("Nome: ")).capitalize()

    sexo = str(input('Sexo [H/M]: ')).upper()[0]
    while sexo not in 'HM':
        linha()
        sexo = str(input('Invalido!\nSexo [H/M]: ')).upper()[0]
    pessoa['sexo'] = sexo

    idade = int(input('Idade: '))
    while idade < 0 or idade > 100:
        linha()
        idade = int(input('Invalida!\nIdade: '))
    pessoa['idade'] = idade

    galera.append(pessoa.copy())

    choice = str(input('Quer continuar? [S/N] ')).upper()[0]
    escolha(choice)
    if choice in 'N':
        break

print(f'Foram cadastradas {len(galera)} pessoas.')

for pos, pessoa in enumerate(galera):
    for ind, valor in pessoa.items():
        if ind  in 'idade':
            somaidade+=valor

print(f'A média de idade da galera é {somaidade/len(galera):.2f} anos.')

print('As mulheres cadastradas foram: ')
for pos, pessoa in enumerate(galera):
    for ind, valor in pessoa.items():
        if ind in 'sexo' and valor in 'mM':
            print(pessoa['nome'])

for pos, pessoa in enumerate(galera):
    if pessoa['idade'] > (somaidade/len(galera)):
        print(pessoa['nome'],end=' ')
        print(pessoa['idade'])