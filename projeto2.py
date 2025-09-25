import json
import os
import time
#Sistema de gerenciamento de biblioteca, estruturando o  código em classes e objetos, aplicando encapsulamento, métodos e construtores.
class Livro:
    def __init__(self, nome, autor, ano_publicacao):
        self.__titulo = nome
        self.__autor = autor
        self.__ano_publicacao = ano_publicacao
        self.__disponivel = True
    
    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome
    
    def emprestar(self):
        if self.__disponivel:
            self.__disponivel = False
            return True
        return False

    def devolver(self):
        self.__disponivel = True

    def esta_disponivel(self):
        return self.__disponivel

    def get_info(self):
        return f"{self.__titulo} por {self.__autor}, {self.__ano_publicacao}"
    
class biblioteca:
    def __init__(self, nome, autor, ano_publicacao, cadastrar, listar, atualizar, excluir):
        super().__init__(nome, autor, ano_publicacao)
        self.__cadastrar = cadastrar
        self.__listar = listar
        self.__atualizar = atualizar
        self.__excluir = excluir
    
    @property
    def cadastrar(self):
        return self.__cadastrar
    @cadastrar.setter
    def cavaleiro(self, cadastrar):
        self.__cadastrar = cadastrar
    
    def cadastro(self, cadastrar):
        nome = input("Digite o nome: ")
        cadastrar.nome = nome
        autor = input("Digite o autor: ")
        cadastrar.autor = autor
        ano_publicacao = input("Digite o ano de publicação: ")
        cadastrar.ano_publicacao = ano_publicacao

    @property
    def listar(self):
        return self.__listar
    @listar.setter
    def listar(self, lista):
        self.__listar = lista
    #livros disponiveis na biblioteca
    def listar(self, listar):
        print(f"Nome: {listar.nome}, Autor: {listar.autor}, Ano de Publicação: {listar.ano_publicacao}")
        time.sleep(2)

    @property
    def atualizar(self):
        return self.__atualizar
    @atualizar.setter
    def atualizar(self, atualizar):
        self.__atualizar = atualizar
    def atualizar(self, atualizar):
        nome = input("Digite o nome do livro que deseja atualizar: ")
        atualizar.nome = nome
        autor = input("Digite o novo autor: ")
        atualizar.autor = autor
        ano_publicacao = input("Digite o novo ano de publicação: ")
        atualizar.ano_publicacao = ano_publicacao


    @property
    def excluir(self):
        return self.__excluir
    @excluir.setter
    def excluir(self, excluir):
        self.__excluir = excluir
    
    def excluir(self, excluir):
        nome = input("Digite o nome do livro que deseja excluir: ")
        excluir.nome = nome
class salvarDados:
    def __init__(self):  
        pass 
    def salvar_dados(self, caminho, dados):
        with open(caminho, 'w', encoding='utf-8') as f:
            json.dump(dados, f, ensure_ascii=False, indent=4)    
    def carregar_dados(self, caminho):
        if os.path.exists(caminho):
            with open(caminho, 'r', encoding='utf-8') as f:
                return json.load(f)
        return []
def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')
caminho_livros = 'livros.json'
salvar = salvarDados()
livros = salvar.carregar_dados(caminho_livros)
if livros is None:
    livros = []
while True:
    print (8*"-", "BIBLIOTECA PY",8*"-")
    print('1 - Cadastrar Livro')
    print('2 - Listar Livros Disponíveis')
    print('3 - Atualizar Livro')
    print('4 - Excluir Livro')
    print('5 - Sair do Sistema')

    opcao = input('digite a area: ')
    limpar()
    match opcao:
        case '1':
            titulo = input('Informe o título do livro: ')
            autor = input('Informe o autor do livro: ')
            ano_publicacao = input('Informe o ano de publicação do livro: ')
            novo_livro = Livro(titulo, autor, ano_publicacao)
            livros.append({
                'titulo': titulo,
                'autor': autor,
                'ano_publicacao': ano_publicacao,
                'disponivel': novo_livro.esta_disponivel()
            })
            salvar.salvar_dados(caminho_livros, livros)
            limpar()
            print('Livro cadastrado com sucesso!')
            time.sleep(2)
        case '2':
            print('LIVROS DISPONÍVEIS NA BIBLIOTECA')
            for livro in livros:
                status = 'Disponível' if livro['disponivel'] else 'Indisponível'
                print(f"Título: {livro['titulo']}, Autor: {livro['autor']}, Ano: {livro['ano_publicacao']}, Status: {status}")
            time.sleep(3)
        case '3':
            nome_antigo = input('Digite o nome do livro que deseja atualizar: ').strip()
            encontrado = False
            for livro in livros:
                if livro['titulo'].lower() == nome_antigo.lower():
                    novo_nome = input('Digite o novo nome do livro: ').strip()
                    livro['titulo'] = novo_nome
                    encontrado = True
                    break
        case '4':
            nome_antigo = input('Digite o nome do livro que deseja excluir: ').strip()
            encontrado = False
            for i, livro in enumerate(livros):
                if livro['titulo'].lower() == nome_antigo.lower():
                    del livros[i]
                    encontrado = True
                    break        
            if encontrado:
                salvar.salvar_dados(caminho_livros, livros)
                print(f'Livro "{nome_antigo}" atualizado com sucesso!')
            else:
                print(f'Livro "{nome_antigo}" não encontrado!')
            time.sleep(2)