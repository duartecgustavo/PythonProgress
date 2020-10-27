# ----------------// INTERFACE \\---------------------

def linha():
    print('-' * 42)

def titulo(titulo):
    linha()
    print(f"{titulo:^42}")
    linha()

def leiaInt(msg):
    while True:
        try:
            inte = int(input(msg))
        except Exception:
            print('\033[31mERRO! Por favor digite um numero inteiro valido!\033[m')
        except (KeyboardInterrupt):
            print('Entrada de dados interrompida pelo usuario!')
            return 0
        else:
            return inte

def menu(lista):
    titulo('CADASTRAR NOVA PESSOA')
    c=1
    for item in lista:
        print(f'{c} - {item}..')
        c+=1
    linha()
    opc = leiaInt('Sua opção? ')
    return opc

# ----------------// ARQUIVO \\---------------------

def arquivo(nome):
    try:
        a = open(nome,'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um erro na criação!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


def lerArquivo(arq):
    try:
        a = open(arq, 'rt')
    except:
        print('Erro na leitura!')
    else:
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()


def cadastrar(arq, nome = 'desconhecido', idade = 0):
    try:
        a = open(arq, 'at+')
    except:
        print('Erro ao abrir o arquivo!')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Erro ao adicionar os dados')
        else:
            print(f'Novo registro adicionado de {nome};')
            a.close()