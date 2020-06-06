# Desafio 2 : Primeiro 'input' e lista com cores.

nome = input('Digite seu nome: ')
cor = {'azul' : '\033[34m',
       'limpa' : '\033[m'}
print(f'Seu nome é,\033[34m{nome}{cor["limpa"]}!')
print(f'Seu nome é \033[34m{nome}\033[m!')