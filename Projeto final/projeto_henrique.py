import json
import os
import time

usuario = []
nome_arquivo = ""

limpar = lambda: os.system('cls' if os.name == 'nt' else 'clear')

usuarios = []

# Caminho do arquivo dos livros para o JSON
caminho_livros = 'C:\\Users\\ead\\Documents\\Logica de programação\\Henrique07\\livros.json'

# Carrega os livros do arquivo, caso exista
if os.path.exists(caminho_livros):
    with open(caminho_livros, 'r', encoding='utf-8') as f:
        usuarios = json.load(f)
else:
    usuarios = []

while True:
    print('1 - Cadastre do Livro ')
    print('2 - Livros disponiveis ')
    print('3 - Atualizar lista ')
    print('4 - Excluir livros ')
    print('5 - Sair do sistema ')

    opcao = input('Digite a opção desejada: ')
    limpar()
    match opcao:
        #Primeira etapa o cadastro do livro
        case '1':
            usuario = {}
            usuario['Livro: '] = input('Informe o Nome do livro: ')
            usuarios.append(usuario)
            with open(caminho_livros, 'w', encoding='utf-8') as f:
                json.dump(usuarios, f, ensure_ascii=False, indent=4)
            limpar()
            print('Livro cadastrado com sucesso!')
            continue
        case '2':
            #Segundo é listar os livros disponiveis adicionados pelo o usuario
            print('LIVROS DISPONIVEIS NA BIBLIOTECA')
            for usuario in usuarios:
                for chave in usuario:
                    print(f'{chave.capitalize()} : {usuario.get(chave)}')
                print('-'*40)
            time.sleep(3)
            continue
        #Qual o livro que deve atualizar e logo em seguida o livro que o usuario deseja colocar no lugar
        case '3':
            nome_antigo = input('Digite o nome do livro que deseja atualizar: ').strip()
            encontrado = False
            for usuario in usuarios:
                if usuario['Livro: '].lower() == nome_antigo.lower():
                    novo_nome = input('Digite o novo nome do livro: ').strip()
                    usuario['Livro: '] = novo_nome
                    encontrado = True
                    break
            if encontrado:
                with open(caminho_livros, 'w', encoding='utf-8') as f:
                    json.dump(usuarios, f, ensure_ascii=False, indent=4)
                print(f'Livro "{nome_antigo}" atualizado com sucesso!')
            else:
                print(f'Livro "{nome_antigo}" não encontrado!')
            continue
        #excluir os livros que tem na biblioteca
        case '4':
            nome_excluir = input('Digite o nome do livro que deseja excluir: ').strip()
            novo_usuarios = [usuario for usuario in usuarios if usuario['Livro: '].lower() != nome_excluir.lower()]
            if len(novo_usuarios) < len(usuarios):
                usuarios = novo_usuarios
                with open(caminho_livros, 'w', encoding='utf-8') as f:
                    json.dump(usuarios, f, ensure_ascii=False, indent=4)
                print(f'Livro "{nome_excluir}" excluído com sucesso!')
            else:
                print(f'Livro "{nome_excluir}" não encontrado!')
            continue
        #sair do sistema
        case '5':
            print('Saindo do sistema...')
            time.sleep(2)
            break