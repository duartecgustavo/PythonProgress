# Desafio 112 - Aula 22: Programa que valide o salario e garanta que receberáapenas valores monetários.

import Modulos

salario = Modulos.validanum('Seu salario: ')
aumento = float(input(f'Quantos % deseja aumentar no seu salario {Modulos.format(salario)}? '))
reajuste = float(input(f'Quantos % será reduzido em seu salario {Modulos.format(salario)}? '))

Modulos.notinha(salario, aumento, reajuste)