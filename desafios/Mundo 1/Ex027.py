# Desafio 27 - Aula 9 : Leia o nome completo de uma pessoa mostrando em seguida o primeiro e o ultimo nome!

nome = input('Digite o seu \033[4mnome completo\033[m: ').strip().split()
print (f'Seu nome começa com \033[34m{nome[0].title()}\033[m e termina com \033[34m{nome[-1].title()}\033[m!')