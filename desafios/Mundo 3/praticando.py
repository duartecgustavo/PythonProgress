# Desafio 94 - Aula 19 : Programa que leia NOME, SEXO e IDADE de varias pessoas, guarde cada dado em um dicionario e ao fim mostre:
# A/ Quantas pessoas foram cadastradas.
# B/ Média de idade do grupo.
# C/ Lista com todas as mulheres.
# D/ Lista com todas as pessoas com IDADE acima da média.

pessoa = {}
galera = []
somaidade=0

while True:
        
    pessoa['nome'] = str(input('Nome: ')).capitalize()

    sexo= str(input('Sexo[[H/M]]: ')).upper()[0]
    while sexo not in 'HM':
        sexo= str(input('Invalido!\nSexo[[H/M]]: ')).upper()[0]
    pessoa['sexo'] = sexo

    idade= int(input('Idade: '))
    somaidade+=idade
    pessoa['idade'] = idade

    galera.append(pessoa.copy())

    choice = str(input('Quer continuar? [S/N]')).upper()[0]
    print('=-'*15)
    while choice not in 'SN':
        choice = str(input('Opção invalida!\nQuer continuar? [S/N]')).upper()[0]
        print('=-'*15)
    if choice in 'N':
        break    
media = somaidade/len(galera)
print(f'Foram cadastradas {len(galera)} pessoas.')

print(f'A média de idade da galera é {media}')

print('A mulheres cadastradas foram: ')
for pos, pess in enumerate(galera):
    if pess['sexo'] in 'M':
        print(pess['nome'])
print(f'Pessoa acima da  média de idade que é {media}: ')
for pos, pess in enumerate(galera):
    if pess['idade'] > media:
        print(pess['nome'])
