# Desafio 76 - Aula 16 : Programa que tenha apenas uma TUPLAS com os nomes de produtos e seus respectivos preços:
# No final mostre a listagem de preços de forma TABULAR.

total = 0

print('-'*40)
print(f'{"LISTAGEM DE PREÇOS":^36}')
print('-'*40)

produtos = ('pão', 0.50, 'mussarela', 3, 'mortadela', 2.50, 'calabresa', 4.50, 'manteiga', 8, 'leite', 9.50)

for item in produtos:
    if produtos.index(item) % 2 == 0:
        print(f'{f"{item}":.<30}R$', end='')
    else:
        print(f'{item:>5.2f}')
        total+=item

print('='*40)
print(f'{"Total":.<30}R$', end=f'{total:>5.2f}')

# OUUU

'''for i in produtos:
    if type(i) is str:
        print(f'{i:.<32}', end='')
    else:
        print(f'R$ {i:>5.2f}')
print('--'*20)'''
