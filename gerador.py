from random import choice
import string
from time import sleep

def Arquivo_Existe(nome_arquivo):
    try:
        a = open(nome_arquivo, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def Criar_Arquivo(nome_arquivo):
    try:
        a = open(nome_arquivo, 'wt+')
        a.close()
    except:
        print('houve um erro')


def Adicionar_Arquivo(nome_arquivo,senha):
    try:
        a = open(nome_arquivo, 'at')
    except:
        print('houve um erro')
    else:
        try:
            a.write(f'{senha}\n')
        except:
            print('erro ao inserir dado')
        else:
            print('adicionando senha...')
            sleep(1)
            print(f'{senha} adicionado com sucesso')


def Ler_Arquivo(nome_arquivo):
    global dado
    try:
        a = open(nome_arquivo, 'rt')
    except:
        print('houve algum erro')
    else:
        for linha in a:
            dado = linha
            print(f'{dado}')
    finally:
        a.close()

def Gerar_Senha(valor, tamanho):
    senha = ''
    for i in range(tamanho):
        senha += choice(valor)
    return senha

arq = 'senhas.txt'
if not Arquivo_Existe(arq):
    Criar_Arquivo(arq)

while True:
    print('-'*42)
    print('Gerador de senha'.center(42))
    print('-'*42)
    print("""
    1 - Gerar senha 
    2 - Ler senhas
    3 - Sair
    """)

    escolha = int(input('Digite a usa opção: '))
    if escolha == 3:
        break
    elif escolha == 2:
        print('-_'*21)
        print('Lista de senhas'.center(42))
        Ler_Arquivo(arq)
        print('-_' * 21)
    else:
        while True:
            print('-' * 42)
            print('Opções'.center(42))
            print('-' * 42)
            print("""
            A - Números
            B - Números + Letras
            C - Números + Letras + Algarísmo especial
            D - Sair
            """)

            opc = input('Digite sua opção: ')
            if opc == 'd' or opc == 'D':
                break
            elif opc == 'a' or opc == 'A':
                tam = int(input('Digite o tamanho da senha: '))
                Adicionar_Arquivo(arq, Gerar_Senha(string.digits, tam))
                break
            elif opc == 'b' or opc == 'B':
                tam = int(input('Digite o tamanho da senha: '))
                Adicionar_Arquivo(arq, Gerar_Senha(string.digits + string.ascii_letters, tam))
                break
            elif opc == 'c' or opc == 'C':
                tam = int(input('Digite o tamanho da senha: '))
                Adicionar_Arquivo(arq, Gerar_Senha(string.digits + string.ascii_letters + string.punctuation, tam))
                break