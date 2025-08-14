
nome = input('Digite seu nome: ')
cpf = input('Digite seu CPF: ')
telefone = input('Digite seu telefone: ')
dt_nascimento = input('Digite sua data de nascimento: ')
print(80*'=')

while True:
    print(30*"-", "Sistema console 2 DS",30*"-")
    print('1 - Calculadora IMC')
    print('2 - Maioridade')
    print('3 - Calculadora')
    print('4 - Dados pessoais')
    print('5 - Feliz Natal')
    print('6 - Sair')

    opção = input('Digite uma opção: ')
        
    if opção == '1': 
        while True:
            altura = float(input('Digite a sua altura:'). replace(',',','))
            peso = float(input('Digite o seu peso:').replace(',',','))
            
            IMC = peso / (altura * altura) 
            print()
            print(f'Seu IMC é: {IMC:.2f}')

            if IMC <= 18.5:
                print('Classificação: Abaixo do normal')
            elif IMC <= 24.9:
                print('Classificação: Peso normal')
            elif IMC <= 29.9:
                print('Classificação sobre peso')
            elif IMC <=34.9:
                print('Obesidade grau I')
            elif IMC <=39.9:
                print('Obesidade grau II')
            else:
                print('Obesidade grau III')

            opção = input("Digite uma opção: ")

            if opção == 's':
                continue
            elif opção == 'n':
                print('Saindo do sistema')
                break
            else:
                print('Opção invalida')
    elif opção == '2': 
            pass 
    elif opção == '3': 
        while True:
            

            print("Calculadora")
            print("1 - Soma")
            print("2 - Divisão")
            print("3 - Subtração")
            print("4 - Multiplicação")
            print("5 - Sair")
            num1 = float(input('Digite o primeiro numero: '))
            num2 = float(input('Digite o segundo numero: '))

            opção_calculo = input('Escolha uma operação matemática: ')

            if opção_calculo == '1':
                    print(f'Resultado da soma é: {num1 + num2}')
            elif opção_calculo == '2':
                    print(f'Resultado da divisão é: {num1 / num2}')
            elif opção_calculo == '3':
                    print(f'Resultado da subtração é: {num1 - num2}')
            elif opção_calculo == '4':
                    print(f'Resultado da multiplicação é: {num1 * num2}')
            elif opção_calculo == '5':
                print (f'Resultado da exponenciação é:{num1 * num2}')
                break
            else:
                print("Opção Inválida")
    elif opção == '4': 
            print(50*'_')
            print(f'Nome:{nome} | Telefone: {telefone}     |')
            print(f'Cpf: {cpf} | Data de nascimento {dt_nascimento}    |')
            print(50*'_')
    elif opção == '5': 
            linhas = 15
            j = 1

            while j<= linhas:
                espacos = linhas - j
                estrelas = 2 * j - 1 

                print(" " * espacos +"*" * estrelas)
                j +=1
    elif opção == "6":
            print("Saindo do sistema")
            break
    else:
        print('Opção invalida:')


            
