# Desafio 2 - Aula 5 : Primeiro 'input' e lista simplês com cores.

nome = input('Me diga seu nome: ')
cor = {'azul' : '\033[34m',
       'limpa' : '\033[m'}
print(f'Seu nome é,\033[34m{nome}{cor["limpa"]}!')
print(f'Seu nome é \033[34m{nome}\033[m!')