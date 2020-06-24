# Desafio 06 - Aula 7 : Leia um numero e mostre seu dobro, triplo e raiz quardrada.

numero = int(input('\033[31mDigite um numero\033[m: '))

print('O \033[33mdobro\033[m deste numero é \033[34m{}\033[m, seu \033[33mtriplo\033[m é \033[34m{}\033[m e sua \033[31mraiz quadrada\033[m é \033[34m{:.3f}\033[m!!!'.format(numero*2, numero*3, pow(numero,(1/2)))) # pow também representa raiz² assim como numero**(1/2)