# Desafio 43 - Aula 12 : Programa que calcule o IMC e apresente  a tabela:
# A/ Abaixo de 18.5 - ABAIXO DO PESO.
# B/ Entre 18.5 e 25 - PESO IDEAL.
# C/ De 25 até 30 - SOBREPESO.
# D/ 30 até 50 - OBESIDADE.
# E/ Acima de 40 - OBESIDADE MORBIDA.
# FORMULA - ALTURA² / PESO

print('='*50)
nome = 'IMC (INDICE DE MASSA CORPORAL) FREE'
print(f'{nome:^50}')
print('='*50)

altura = float(input('Me diga sua altura: (m)'))
peso = float(input('Agora me diga seu peso atual: (KG)'))
imc = peso/(altura**2)

if imc < 18.5:
    print(f'Seu imc é {imc:.1f}!\nVocê está ABAIXO DO PESO ideal! Coma mais.')
elif 18.5 <= imc < 25:
    print(f'Seu imc é {imc:.1f}!\nVocê está no PESO IDEAL. Continue assim!')
elif 25 < imc <= 30:
    print(f'Seu imc é {imc:.1f}!\nVocê está com SOBREPESO! Se cuide e pratique exercicios.')
elif 30 < imc <= 50:
    print(f'Seu imc é {imc:.1f}!\nVocê está com OBESIDADE, pratique exercicios, controle sua alimentação e se possivel consulte um médico.')
else:
    print(f'Seu imc é {imc:.1f}!\nATENÇÃO! Procure um médico especialista para lhe orientar sobre seu peso. Sua saúde está em risco!')