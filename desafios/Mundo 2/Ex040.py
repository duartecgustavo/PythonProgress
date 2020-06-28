# Desafio 40 - Aula 12 : Programa que leia algumas notas e informe:
# A/ Média abaixo de 5.0 é - REPROVADO.
# B/ Média entre 5.0 e 6.9 - RECUPERAÇÃO.
# C/ Média maior que 7.0 é - APROVADO.
# EE/ Média > 9,8 PARABÉNS VOCÊ É UM GENIO.

nota1 = float(input('Digite sua nota de matematica do primeiro bimestre: '))
nota2 = float(input('Agora digite sua nota do segundo bimestre: '))
media = (nota1 + nota2) / 2

if media < 5.0:
    print('\nInfelismente você foi \033[4:31mREPROVADO\033[m!'
          f'\nSua média foi de \033[34m{media:1f}\033[m, que está abaixo do minimo de 5.0 pontos para recuperação e de 8.0 pontos para ser aprovado.'
          '\n\nEstude mais!!!')
elif media > 4.9 and media <= 7.9:# 7.9 => media > 4.9
    print('\nVocê está de \033[4:32mRECUPERAÇÃO\033[m!'
          f'\nSua média é de \033[32m{media:.1f}\033[m pontos, você precisa estudar para conseguir mais {8.0-media} pontos e atingir o minimo de 8.0 para ser APROVADO!'
          
          '\n\nEstude mais!!!')
elif media > 7.9 and media <= 9.7:# 9.7 >= media > 7.9
    print('\nParabéns você está \033[4:34mAPROVADO\033[m!'
          f'\nSua média foi de \033[32m{media:.1f}\03[m pontos!'
          '\n\nContinue assim! A educação é a chave.')
else:
    print('\n\033[32mPARABÉNS! VOCÊ É UM GENIO!!!\033[m'
          '\nVá até o armario numero 4 e coloque a senha no cadeado 9³/² e pegue o \033[36mCHOCOLATE SECRETO para os GENIOS!\033[m'
          '\n\nContinue sempre assim!!!')
