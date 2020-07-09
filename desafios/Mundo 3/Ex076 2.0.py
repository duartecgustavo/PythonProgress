# Desafio 76 - Aula 16 : Com lista.

produtos = []
total = 0

print('-'*40)
print(f'{"LISTAGEM DE PREÇOS":^36}')
print('-'*40)

while True:
    produto = str(input('Diga o produto: '))
    produtos.append(produto)
    preco = float(input(f'{produto} preço R$'))
    produtos.append(preco)

    choice = str(input('Quer continuar?[S/N] ')).upper()[0]
    while choice not in 'SN':
        choice = str(input('\033[31mOpção invalida!\033[m\nQuer continuar?[S/N] ')).upper()[0]
    if choice in 'N':
        break

print('_'*50)

for item in produtos:
    if type(item) is str:
        print(f'{item:.<40}R$',end=' ')
    if type(item) is float or type(item) is int:
        print(f'{item:>4.2f}')
        total+=item
print('_'*50)

print(f'{"total":.<40}R$', f'{total:>4.2f}')
