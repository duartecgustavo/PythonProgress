# Desafio 15 - Aula 07 : Programa que leia a quantidade KM rodados por um carro alugado e a quantidade de dias que este carro ficou alugado, sabendo que o valor do aluguel por 
# dia é R$60 e o valor por KM rodado é R$0.15.

aluguel = int(input('Por quantos dias você utilizou este carro? '))
kmrodado = int(input('Quantos KM foram rodados com este carro? '))
print(f'O valor a ser pago por \033[31m{aluguel} dias\033[m de uso e \033[31m{kmrodado}KM\033[m rodados é de: \033[33mR${(aluguel*60)+(kmrodado*0.15):.2f}\033[m!')
