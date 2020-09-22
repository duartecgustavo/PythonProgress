# Modularização - dividir o programa emm pedaços

# Exemplo: 

def fatorial (num):
    f=1
    for c in range(1, num+1):
        f*=c
        print(f)
    return f

def dobro(num):
    num+=num
    return num

def triplo(num):
    return num * 3

num = int(input('Um numero: '))
fat = fatorial(num)
print(f'O fatorial de {num} é {fat}!')

# Após criar uma função eu posso colocar esta função em outra pasta dentro do meu  arquivo com o programa
# E importar essas funções para meu programa principal

# Crios dois arquivos - 'uteis.py' e 'programa.py'

# 'uteis.py'ficara minha função

def fatorial (num):
    f=1
    for c in range(1, num+1):
        f*=c
        print(f)
    return f

def dobro(num):
    num+=num
    return num

def triplo(num):
    return num * 3

# programa.py

import uteis

num = int(input('Um numero: '))
fat = uteis(fatorial(num))
print(f'O fatorial de {num} é {fat}!')
print(uteis.dobro(num))
print(uteis.triplo(num)) 