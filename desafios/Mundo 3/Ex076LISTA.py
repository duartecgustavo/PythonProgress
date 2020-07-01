# Desafio 76 - Aula 16 : Programa que tenha apenas uma TUPLAS com os nomes de produtos e seus respectivos preços;
# No final mostre a listagem de preços de forma TABULAR.

total = 0

print('-'*40)
print(f'{"LISTAGEM DE PREÇOS":^36}')
print('-'*40)

produtos = ('pão', 0.50, 'mussarela', 3, 'mortadela', 2.50, 'calabresa', 4.50, 'manteiga', 8, 'leite', 9.50)

for c in produtos:
    if produtos.index(c) % 2 == 0:
        print(f'{f"{c}":.<30}R$', end='')
    else:
        print(f'{c:>5.2f}')
        total+=c

print('='*40)
print(f'{"Total":.<30}R$', end=f'{total:>5.2f}')

# OUUU

'''for i in produtos:
    if type(i) is str:
        print(f'{i:.<32}', end='')
    else:
        print(f'R$ {i:>5.2f}')
print('--'*20)'''
