# Desafio 45 - Aula 12 : JOKENPÔ - PEDRA PAPEL E TESOURA!

import random
import time
print('='*50)
print(f'{" BEM VINDO AO JOKENPÔ CONTRA O BOLSONARO ":-^50}')
print('='*50)

choice = 'S'
while choice == 'S':

    print('''\nSelecione uma das três opções:
    PEDRA   - NA CABEÇA DO BOLSONARO
    TESOURA - PARA CORTAR A CABEÇA DO BOLSONARO
    PAPEL   - PARA QUEIMAR O BOLSONARO''')

    escolha = input('\nEscreva sua escolha: ').lower()

    lista = ['pedra', 'papel', 'tesoura']
    pc = random.choice(lista)

    print('JO')
    time.sleep(0.5)
    print('KEN')
    time.sleep(0.5)
    print('PÔ!!!')

    if escolha == 'pedra' or escolha == 'papel' or escolha == 'tesoura':
        if escolha == pc:
            print('\nEMPATE!')
            print(f'\nSua esolha foi {escolha.upper()}!\nVs\nA escolha do computador que foi {pc.upper()}!')
        elif escolha == 'pedra' and pc == 'papel':
            print(f'\nCOMPUTADOR GANHOU!!! O BOZO VAI QUEIMAR!')
            print(f'\nSua esolha foi {escolha.upper()}!\nVs\nA escolha do computador que foi {pc.upper()}!')
        elif escolha == 'pedra' and pc == 'tesoura':
            print(f'\nVOCÊ GANHOU!!! CHUVA DE PEDRAS NO BOZO!')
            print(f'\nSua esolha foi {escolha.upper()}!\nVs\nA escolha do computador que foi {pc.upper()}!')
        elif escolha == 'papel' and pc == 'pedra':
            print(f'\nVOCÊ GANHOU!!! O BOZO VAI QUEIMAR!')
            print(f'\nSua esolha foi {escolha.upper()}!\nVs\nA escolha do computador que foi {pc.upper()}!')
        elif escolha == 'papel' and pc == 'tesoura':
            print(f'\nCOMPUTADOR GANHOU!!! CORTE A CABEÇA DO BOZO!')
            print(f'\nSua esolha foi {escolha.upper()}!\nVs\nA escolha do computador que foi {pc.upper()}!')
        elif escolha == 'tesoura' and pc == 'pedra':
            print(f'\nCOMPUTADOR GANHOU!!! CORTE A CABEÇA DO BOZO!')
            print(f'\nSua escolha foi {escolha.upper()}!\nVs\nA escolha do computador que foi {pc.upper()}!')
        elif escolha == 'tesoura' and pc == 'papel':
            print(f'\nVOCÊ GANHOU!!! CORTE A CABEÇA DO BOZO!')
            print(f'\nSua esolha foi {escolha.upper()}!\nVs\nA escolha do computador que foi {pc.upper()}!')
    else:
        print('\nEscreva corretamente sua arma!')

    choice = str(input('Jogar novamente?[S/N] ')).upper()
    
time.sleep(0.5)
print('Fim do jogo!')
