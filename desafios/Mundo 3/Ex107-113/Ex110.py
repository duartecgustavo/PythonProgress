# Desafio 110 - Aula 22: Ao passar os mesmos parametros dos exerciocios anteriores, o programa de trazer
# um resumo formatado com as mesmas informação dos outro;

import Modulos

salario = float(input('Informe seu salario: '))
Modulos.valida(salario)
aumento = int(input(f'Quantos % deseja aumentar no seu salario {salario}?'))
reajuste = int(input(f'Quantos % será reduzido em seu salario {salario}?'))

Modulos.notinha(salario, aumento, reajuste) 