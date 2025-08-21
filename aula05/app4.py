import os

while True:
    try:
        novo_texto = input('Digite o texto: \n')
        nome_arquivo = input('Digite o nome do seu arquivo (sem extensão): ').strip().lower()

        with open(fr'C:\Users\ead\Documents\Logica de programação\Henrique07\aula05{nome_arquivo}.txt', 'w', encoding='utf-8') as f:
            f.write(novo_texto)

        os.system('cls' if os.name == 'nt' else 'clear')
        print(f'{nome_arquivo}.txt gravado com sucesso.')


        novo_textoo = input('Digite o novo texto: \n')

        with open(fr'C:\Users\ead\Documents\Logica de programação\Henrique07\aula05{nome_arquivo}.txt', 'a', encoding='utf-8') as f:
            f.write(f'\n{novo_textoo}')
        print('Gravado com sucesso.')

        #ler os dados atualizados
        with open(f'{nome_arquivo}.txt', 'r', encoding='utf-8') as f:
            texto_final = f.read()
        print(f'Texto final: {texto_final}')

        while True:
            prosseguir = input('Deseja abrir outro arquivo ? (s/n): ').strip().lower()
            if prosseguir == 's' or prosseguir == 'n':
                break
            else:
                print('opçao invalida!')
                continue
        match prosseguir:
            case's':
                continue
            case 'n':
                break
    except Exception as e:
        print(f'Não foi possivel ler o arquivo. {e}')
        continue