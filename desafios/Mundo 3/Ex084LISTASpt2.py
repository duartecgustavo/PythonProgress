# Desafio 84 - Aula 18 : Programa que leia o NOME e o PESO de varias pessoas, depois mostre:
# A/ Quantas pessoas foram cadastradas.
# B/ As pessoas mais pesadas.
# C/ As pessoas mais leves.

pessoas = []
galera = []
pesos = []
nomemaispesado = []
nomemaisleve = []

while True:
    pessoas.append(str(input('Diga seu nome: ')))
    pessoas.append(float(input('Seu peso: ')))

    galera.append(pessoas[:])
    pessoas.clear()

    choice = str(input('Quer continuar? [S/N]')).upper()[0]
    while choice not in 'SN':
        choice = str(input('Opção invalida!\nQuer continuar? [S/N]')).upper()[0]
    if choice in 'N':
        break

print(f'Foram cadastradas {len(galera)} pessoas.')

for indi in galera:
    pesos.append(indi[1])

for indi in galera:

    if indi[1] == max(pesos):
        nomemaispesado.append(indi[0])
    elif indi[1] == min(pesos):
        nomemaisleve.append(indi[0])

print(f'O maior peso foi {max(pesos)}kg de {nomemaispesado}.')
print(f'O menor peso foi {min(pesos)}kg de {nomemaisleve}.')