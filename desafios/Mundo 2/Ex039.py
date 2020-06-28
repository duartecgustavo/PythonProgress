# Desafio 39 - Aula 12 : Programa que leia o ano de nascimento de um jovem e informe de acordo com sua idade :
# A/ Se ele ainda vai se alistar ao exercito.
# B/ Se ele ja deve se alistar ao exercito.
# C/ Se ja passou da hora de ele se alistar.
# Mostre também o tempo que falta ou que passou da sua idade de alistamento.

from datetime import date

print('<-'*30)
print(f'\033[32m{"PROGRAMA DE ALISTAMENTO AO EXERCITO ANTI-FACISTA DO BRASIL":^60}\033[m')
print('->'*30)

nome = str(input('Primeiramente queremos saber seu \033[4mnome completo\033[m! '))
nascimento = int(input('Agora digite seu \033[4mano de nascimento\033[m: '))

print(f'\n')

if date.today().year-nascimento < 18: # Caso o ano de nascimento menos o ano em que estamos seja menor que 18.
    print(f'''\033[34m{nome.title().split()[0]}\033[m, você ainda \033[31mnão esta na idade\033[m de entrar no batalhão anti-facista Brasileiro!
\nAinda deve esperar \033[32m{18-(date.today().year-nascimento)} anos\033[m para chegar sua vez, retorne a sub-preitura em \033[32m{date.today().year + (18-(date.today().year-nascimento))}\033[m, após concluir seus 18 anos. 

Até mais!!!''')

elif date.today().year-nascimento == 18:
    print(f'''\n\033[34m{nome.title().split()[0]}\033[m chegou a sua hora de \033[31mquebrar alguns Facistas na porrada!!!\033[m
          \033[4mSe apresente na sub-prefeitura\033[m mais proxima com:
          \033[32m- RG
          - Comprovante de Residencia\033[m

Não perca tempo! Pois os facistam não esperam, eles matam!

Te vejo por lá!''')
else:
    print(f'''Já passou da hora \033[34m{nome.title().split()[0]}\033[m! Você deveria ter se alistado com \033[31m18 anos em {date.today().year-((date.today().year-nascimento)-18)}\033[m!
\nEntre em contato com o \033[4mserviço de alistamento Anti-Facista do Brasil\033[m e vá quebrar a cara de alguns Facistas!

Te vejo por lá!''')