# Desafio 71 - Aula 15 : Programe um caixa eletronico que. Pergunte ao usuario qual valor a ser sacado(numero inteiro) e o programa deve informar quantas CEDULAS
#de cada valor serão entregues. OBS: Podem ser cédulas de R$50 R$20 R$10 R$1.

print('='*50)
print(f'{"BANKAST":^50}')
print('='*50)
count50 = n50 = n20 = n10 = n1 = 0
choice = ' '

while True:
    valor = int(input('Quanto você quer sacar? '))
    while True:
        if valor >= 50:
            n50 += 1
            valor-=50

        elif 20 <= valor < 50:
            n20 += 1
            valor -= 20

        elif 10 <= valor < 20:
            n10 += 1
            valor -= 10

        elif 1 <= valor < 10:
            n1 += 1
            valor -= 1

        else:
            break

    if n50 > 0:
        print(f'Total de {n50} notas de R$50.')
    if n20 > 0:
        print(f'Total de {n20} notas de R$20. ')
    if n10 > 0:
        print(f'Total de {n10} notas de R$10.')
    if n1 > 0:
        print(f'Total de {n1} notas de R$1.')

    choice = str(input('Deseja realizar outra operação?[S/N] ')).upper()[0]
    while choice not in 'SN':
        choice = str(input('\033[31mOpção invalida!\033[m\nDeseja realizar outra operação?[S/N] ')).upper()[0]

    if choice in 'S':
        n50 = n20 = n10 = n1 = 0
    else: break

print('='*50)
print('Volte sempre ao BANKAST.')