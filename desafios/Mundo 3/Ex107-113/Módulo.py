# Módulos para aula 22.

def fatorial(num):
    f = 1
    for c in range(1, num + 1):
        f *= c
        print(f)
    return f

# Desafio 107 - Aula 22: Criar um móodulo chamado moeda.py que tenha funções incorporadas.
# aumentar() | diminuir() | dobro() | metade()
# E desenvolva um programa  que importe este módulo e rode essas funções;

def dobro(num, moeda=False):
    num += num

    # Desafio 109:
    if moeda == True:
        num = format(num)  # o resultado sera formatado pela minha função 'format()'

    return num


def triplo(num, moeda=False):
    # Desafio 109:
    if moeda == True:
        num = format(num)

    return num * 3


def metade(num, moeda=False):
    num = num / 2

    # Desafio 109:
    if moeda == True:
        num = format(num)

    return num


def aumento(num, aum, moeda=False):
    aum = (num * aum) / 100
    num = num + aum

    # Desafio 109:
    if moeda == True:
        num = format(num)

    return num


def reajuste(num, dim, moeda=False):
    reaj = (num * dim) / 100
    num = num - reaj

    # Desafio 109:
    if moeda == True:
        num = format(num)

    return num


# Desafio 108 - Aula22: Crie um módulo que formate as infos enviadas para R$ da maneira correta.

def format(num, moeda='R$'):
    num = (f'{moeda}{num:.2f}'.replace('.', ','))
    return num


# Desafio 109 - Tornar a decisão de formatação uma escolha.


# --------------------------------------------------------//-------------------------------------------------

# Desafio 110 - Aula 22: Ao passar os mesmos parametros dos exerciocios anteriores, o programa de trazer
# um resumo formatado com as mesmas informação dos outro;

def notinha(sal, aum=0, reaj=0):
    linha()
    print(f"{'RESUMO DO SALARIO':^30}")
    linha()
    print(f'Preço analizado: \t{format(sal)}')
    print(f'Dobro salário:  \t{format(dobro(sal))}')
    print(f'Metade salário: \t{format(metade(sal))}')
    print(f'{aum}% de aumento: \t{format(aumento(sal, aum))}')
    print(f'{reaj}% de reajuste: \t{format(reajuste(sal, reaj))}')
    linha()

# --------------------------------------------------------//-------------------------------------------------

# Desafio 112 - Aula 22: Criar um validador de numeros deixando passar apenas numeros
def validanum(sal):
    valido = False
    while valido != True:
        entrada = str(input(sal)).replace(',','.')
        if entrada.isalpha() == True or entrada.strip() == '':
            print(f'ERRO! \"{entrada}\" é invalido!')
        else:
            valido=True
            return float(entrada)

# Validador de caracteres
def validaint(msg):
    ok = False
    valor = 0
    while True:
        numero = str(input(msg))
        if numero.isnumeric():
            ok = True
            valor = int(numero)
        else:
            print('ERROO! Diga um numero inteiro valido!')
        if ok == True:
            break
    return valor

# --------------------------------//-----//--------------------------------67
