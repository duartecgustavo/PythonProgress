# Desafio 22 - Crie u programa que leia  o nome completo de uma pessoa e mostre:
# O nome em todas as letras minusculas e depois maiusculas!
# O nome possui ao sem espaços
# Quantas letras tem apenas o primeiro nome

nome = input(str('Digite seu \033[4:31mnome completo\033[m : ')).strip()
nome1 = nome

#1 e 2
nome.lower()
print (f'Analizando o seu nome, em \033[4mminusculo\033[m fica \033[34m{nome.lower()}\033[m!')
print (f'Analizando o seu nome, em \033[4mMAIUSCULO\033[m fica \033[31m{nome.upper()}\033[m!')

#3
nome = (nome.split())
nome = ''.join(nome)
print (f'Seu nome completo \033[4msem espaços\033[m entre cada nome fica \033[34m{nome}\033[m!\nTotalizando \033[34m{len(nome)}\033[m letras!')
# ouuu
print (f'Seu nome completo \033[4msem espaços\033[m entre cada nome fica \033[34m{nome}\033[m!\nTotalizando \033[34m{len(nome) - nome.count(" ")}\033[m letras!')

#4
nome1 = (nome1.split())
print (f'Seu primeiro nome é \033[34m{(nome1[0])}\033[m e possui \033[31m{len(nome1[0])}\033[m letras!')

