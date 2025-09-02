import json 
import os

usuario = []
nome_arquivo = ""

limpar = lambda: os.system('cls' if os.name == 'nt' else 'clear')

usuarios = []
while True:
    print('1 - Cadastrar seu usuario ')
    print('2 - Salvar arquivo JSON ')
    print('3 - Fazer leitura do JSON ')
    print('4 - Sair do sistema ')

    opcao = input('Digite a opção desejada: ')
    limpar()
    match opcao:
        case '1':
            usuario = {}
            usuario['Nome'] = input('Informe o nome: ').strip().title()
            usuario['Idade'] = input('Informe a idade: ')
            usuario['Email'] = input('Informe o email: ').strip().lower()
            
            usuarios.append(usuario)
            limpar()
            print('Usuário cadastrado com sucesso!')
            continue
        case '2':
            nome_arquivo = input('Informe o nome do arquivo (sem extensão): ').strip().lower()
            caminho_arquivo = f'C:\\Users\\ead\\Documents\\Logica de programação\\Henrique07\\{nome_arquivo}.json'
            with open(caminho_arquivo, 'w', encoding='utf-8') as f:
                json.dump(usuarios, f, ensure_ascii=False, indent=4)
            limpar()
            print(f'Arquivo {nome_arquivo}.json salvo com sucesso!')
        case '3':
            if not nome_arquivo:
                nome_arquivo = input('Digite o nome do arquivo: ').strip().lower()
            caminho_arquivo = f'C:\\Users\\ead\\Documents\\Logica de programação\\Henrique07\\{nome_arquivo}.json'
            try:
                with open(caminho_arquivo, 'r', encoding='utf-8') as f:
                    dados = json.load(f)
                print(30*"-", "USUÁRIOS",30*"-")
                for usuario in dados:
                    for chave in usuario:
                        print(f'{chave.capitalize()} : {usuario.get(chave)}')
                    print('-'*40)
            except FileNotFoundError:
                print(f'Arquivo {nome_arquivo}.json não encontrado!')
            continue
        case '4':
            print('Saindo do sistema...')
            break
    
        case _:
            print('Opção inválida! Tente novamente.')
            continue