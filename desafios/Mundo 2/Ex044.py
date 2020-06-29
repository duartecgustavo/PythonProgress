# Deasfio 44 - Aula 12 : Programa que calcule o valor a ser pago em um produto, considerando:
# Seu preço normal e a condição de pagamento: 
# A/ À VISTA, DINHEIRO/CHEQUE - 10% DE DESCCONTO.
# B/ À VISTA CARTÃO - 5% DE DESCONTO.
# C/ 2X cartão - PREÇO NORMAL.
# D/ 3X OU MAIS NO CARTÃO - 20% DE JUROS.

valor = float(input('Digite o valor do produto: R$ '))

print('[1] - À VISTA DINHEIRO\n[2] - À VISTA CARTÃO\n[3] - 2x CARTÃO\n[4] - 3x CARTÃO ou MAIS')

formapgt = float(input('Agora digite um numero para forma de pagamento[1/4]: '))

if formapgt == 1:
    print(f'Selecionado - À VISTA EM DINHEIRO, o produto terá um DESCONTO de 10%!')
    print(f'Preço de R${valor-(valor*(10/100)):.2f}!')
elif formapgt == 2:
    print(f'Selecionado - À VISTA CARTÃO, o produto terá um DESCONTO de 5%!')
    print(f'Preço de R${valor-(valor*(5/100)):.2f}!')
elif formapgt == 3:
    print(f'Selecionado - 2x CARTÃO, o produto saíra pelo seu preço normal')
    print(f'Preço de R${valor:.2f} parcelado em 2x de R${valor/2:.2f}!')
elif formapgt == 4:
    print(f'Selecionado - 3x CARTÃO ou mais, o produto terá acrescimo de 20% de juros em seu preço!')
    precpar = float(input('Quantas parcelas você deseja fazer? '))
    parcelado = valor + (valor * (20 / 100))
    print(f'Preço de R${parcelado:.2f} parcelado em {precpar:.0f}x de R${parcelado/precpar:.2f} com juros!')
else:
    print('Opção invalida!')