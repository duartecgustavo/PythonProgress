# Desafio 71  - (versão Guanabara) - Aula 15 :

print('='*50)
print(f'{"BANCO CEV":^50}')
print('='*50)

valor = int(input('Quanto deseja sacar? '))
total = valor
ced = 50
totalced = 0

while True:
    if total >= ced:
        total -= ced
        totalced += 1
    else:
        if totalced > 0:
            print(f'Total de {totalced} notas de R$50.')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totalced = 0
        if total == 0:
            break

print('='*50)
print('Voltesempre ao Banco CEV!')