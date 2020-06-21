# Desafio 13 - Aula 07 : Programa que leia o salario de um funcionario e dê o mesmo salário com 15% de aumento!

nome = input('Olá, digite seu nome aqui: ')
s = float(input('Agora digite o valor do seu \033[32msalário\033[m atual R$'))
sa = s + (s * (15 / 100))

print(f'\033[31m{nome}\033[m, \033[7:30mPARABÉNS!\033[m Você teve um \033[4:33maumento de 15%\033[m em seu salário de \033[32m{s}\033[m, agora passara a ganhar \033[34mR${sa}\033[m!')
