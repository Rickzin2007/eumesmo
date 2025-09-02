#crie uma aplicação de banco, onde o usúario se cadastra e criauma conta corrente que começa com saldo de R$0,00. O usuário terá as opções: Criar conta, Exibir dados da conta, depositar valor, Sacar valor, Encerrar conta, Sair do programa (break).

import time
import os

limpar = lambda: os.system('cls' if os.name == 'nt' else 'clear')


#1 etapa de criar função de cadastro
def cadastro():
    global conta_atual
    usuario = input('Informe o nome: ')
    cpf = input('Informe seu CPF: ')
    conta_atual = {
        "Nome": usuario,
        "cpf": cpf,
        "saldo": 0
    }
    limpar()
    print('Usuário cadastrado com sucesso!')


#2 etapa criar a função exibir dados da conta
print()
print()

def dados():
    global conta_atual
    if conta_atual:
        print(f"Nome do Usuario: {conta_atual['Nome']}")
        print(f"CPF: {conta_atual['cpf']}")
        print(f"Saldo do Usuario: R${conta_atual['saldo']:.2f}")
    else: print("Nenhuma conta cadastrada.")

#3 etapa criar a função depositar
def depositar(valor):
    global conta_atual
    if conta_atual:
        if valor > 0:
            conta_atual['saldo'] += valor
            print(f"Depósito de R${valor:.2f} realizado com sucesso.")
        else:
            print("Valor de depósito inválido. Tente novamente.")
    else:
        print("Nenhuma conta cadastrada.")
            

#4 etapa criar a função sacar
def sacar(valor):
    global conta_atual
    if conta_atual:
        if valor > 0 and valor <= conta_atual['saldo']:
            conta_atual['saldo'] -= valor
            print(f"Saque de R${valor:.2f} realizado com sucesso.")
        else:
            print("Saldo insuficiente ou valor inválido. Tente novamente.")
    else:
        print("Nenhuma conta cadastrada.")
#5 etapa criar a função encerrar conta
def encerrar_conta():
    global conta_atual
    if conta_atual:
        print("Conta encerrada com sucesso.")
        conta_atual = None
    else:
        print("Nenhuma conta cadastrada para encerrar.")
usuarios = []
conta_atual = None
limpar()

print (8*"-", "BANCO PY",8*"-")
while True:
    print('1 - Criar conta do banco ')
    print('2 - Dados da conta ')
    print('3 - Depositar valor  ')
    print('4 - Sacar valor  ')
    print('5 - Encerrar conta  ')
    print('6 - Sair do Banco ')
    opcao = input('Digite a opção desejada: ')
    match opcao:
        case '1':
            cadastro()
        case '2':
            dados()
        case '3':
            try:
                valor = float(input("Digite o valor para depositar: "))
                depositar(valor)
            except ValueError:
                print("Valor inválido. Tente novamente.")
        case '4':
            try:
                valor = float(input("Digite o valor para sacar: "))
                sacar(valor)
            except ValueError:
                print("Valor inválido. Tente novamente.")
        case '5':
            encerrar_conta()
        case '6':
            print('Saindo do Banco...')
            time.sleep(5)
            break