# Desafio 29 - Aula 10 : Programa que leia a velocidade de um carro!
# Se essa velocidade foi menor que 80km, nada acontece.
# Porém, caso contrario será aplicada uma multa de R$7,00 por km ultrapassado.

velocidade = float(input('Digite a velocidade do carro ao passar pelo radar: '))

if velocidade >= 80:
    print(f'\033[31m{"ATENÇÃO!":=^75}\n\033[mVocê ultrapassou o \033[4:31mlimite de velocidade de 80km/h\033[m desta via.\nSeu \033[4mregistro de velocidade\033[m é de \033[31m{velocidade}km/h\033[m, ultrapassando em \033[4:31m{velocidade - 80}km\033[m a mais que o limite permitido!')
    print(f'Por conta disto será cobrada uma multa de \033[32mR${(velocidade - 80)*7:.2f}\033[m!')
else:
    print(f'\033[34mTudo OKAY, siga com segurança!!!\033[m')