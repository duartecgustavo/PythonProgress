# Desafio 31 - Aula 10 : Programa que pergunte a distancia de uma viagem, calcule o valor de passagem em 0,50 de a viagem for até 200km de distancia e
# 0,45 se a viagem for maior que isso, ouseja uma longa distancia

nome = input('Olá, digite seu nome ao lado: ').strip()
local = input(f'Agora \033[34m{nome.title()}\033[m, digite o ,\033[4mlocal de destino\033[m: ')
distancia = float(input(f'Para finalizar, informe a \033[4mdistancia\033[m até \033[34m{local.title()}\033[m em KM: '))
if distancia <= 200:
    print(f'O valor de sua passagem até \033[34m{local.title()}\033[m é de \033[32mR${distancia*0.50:.2f}\033[m')
    preço = distancia*0.50# metodo apenas com variaveis no IF
else:
    print(f'O valor de sua passagem até \033[34m{local.title()}\033[m é de \033[32mR${distancia*0.45:.2f}\033[m')
    preço = distancia*0.45## metodo apenas com variaveis no IF
# preço = distancia * 0.50 if distancia <= 200 else preço distancia * 0.45 (MANEIRA SIMPLIFICADA)
print(f'O valor da sua passagem até {local.title()} é de R${preço}!')# apenas o print da resposta