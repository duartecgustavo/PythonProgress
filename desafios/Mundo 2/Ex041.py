# Desafio 41 - Aula 12 : Leia o ano de nascimento de um aluno de natação e mostre a categoria de acordo com sua idade.
# A/ Até 9 anos - MIRIM.
# B/ Até 14 anos - INFANTIL. 
# C/ Até 19 anos - JUNIOR.
# D/ Até 20 anos - SENIOR. 
# E/ Acima - MASTER.

from datetime import date

nasc = int(input('Me diga o seu \033[4mano de nascimento\033[m: '))
datual = date.today().year
idade = datual-nasc

if idade <= 9:
    print(f'Você tem \033[32m{idade} anos\033[m, portanto está enquadrado no grupo dos \033[34mnadadores MIRINS\033[m!')
elif idade <= 14:
    print(f'Você tem \033[32m{idade} anos\033[m, portanto está enquadrado no grupo dos \033[34mnadadores INFATIS\033[m!')
elif idade <= 19:
    print(f'Você tem \033[32m{idade} anos\033[m, portanto está enquadrado no grupo dos \033[34mnadadores JUNIORS\033[m!')
elif idade <= 25:
    print(f'Você tem \033[32m{idade} anos\033[m, portanto está enquadrado no grupo dos \033[34mnadadores SENIORS\033[m!')
else:
    print(f'Você tem \033[32m{idade} anos\033[m, portanto está enquadrado no grupo dos \033[34mnadadores MASTER\033[m!')