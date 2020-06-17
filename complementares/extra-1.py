# Exercicio Extra aula 7 : Programa que leia o preço de um produto e mostre o valor com desconto se pago a vista e se pago parcelado
nome = input('Olá, digite seu nome: ')
preço = float(input('Agora digite o preço do produto que deseja comprar: R$'))
av = preço - (preço*(10/100))
pa = preço + (preço*(10/100))
print(f'{nome}, este produto de R${preço:.2f} custa: \nA vista R${av:.2f} com desconto de 10%. \nParcelado custa R${pa:.2f} com 10% de juros.')