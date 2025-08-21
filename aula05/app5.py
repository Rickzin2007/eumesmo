#importação
import json 
try:
    arquivo = input('Digite o nome do arquivo: '). strip().lower()

    with open(f'{arquivo},json', 'r', encoding='utf-8') as f:
        dados = json.load()

    print(30*"-", "DADOS",30*"-")
    for dado in dados:
        for chave in dado:
            print(f'{chave.capitalize()} : {dado.get(chave)}')
        print('-'*40)
except Exception as e:
    print(f'Não foi possivel ler o arquivo. {e}')