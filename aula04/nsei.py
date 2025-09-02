
'''
programa: Sorteio V.1.0
impotando bibliotecas
Aula 04: 10/08/2025
Random: escolha aleatoria
Descrição: sistema recebe o nome dos candidatos e realiza o sorteio


'''
#importando bibliotecas(lib)
import random

nome1 = input('Digite o primeiro nome: ')
nome2 = input('Digite o segundo nome: ')
nome3 = input('Digite o terceiro nome: ')
nome4 = input('Digite o quarto nome: ')
nome5 = input('Digite o quinto nome: ')

lista_nomes = [nome1, nome2, nome3, nome4, nome5]

escolhido = random.choice(lista_nomes)
print(escolhido)



'''
programa: Sorteio V.2.0
impotando bibliotecas
Aula 04: 10/08/2025
Random: escolha aleatoria
Descrição: sistema recebe o nome dos candidatos e realiza o sorteio
'''


#importando bibliotecas(lib)

import random

lista = []

sair = False

while sair == False:
    nome_candidato = input('Digite os nomes para o sorteio ou enter para sair:')
    if nome_candidato != '':
        #append - adiciona o valor da variavel dentro da lista
        lista.append(nome_candidato)
    else:
        sair = True
escolhido = random.choice(lista)

print("escolhido foi : ", escolhido)

'''
programa: Sorteio V.3.0
impotando bibliotecas
Aula 04: 10/08/2025
Random: escolha aleatoria
Descrição: sistema recebe o nome dos candidatos e realiza o sorteio
'''


#importantdo lih
import random
import time
import os 

lista_nomes = []
lista_sorteados = []

while True:
    nome = input('Digite o nome do candidato ou enter para sair: ')
    if nome:
        lista_nomes .append(nome)
    else:
        break

while True:
    if lista_nomes:
        os.system('cls')  
        escolhido = random.choice(lista_nomes)
        lista_sorteados.append(escolhido)
        #excluir o sorteado da lista original

        '''     
        pop - função, remove pelo indice 
            pop() - remove o ultimo elemento
            pop(0) - remove o indice 0
        del - instrução, remover item pelo indice, mais de um item
            del(1:10)

        remove - remove a partir de uma variavel
        Lista.remove(variavel)
        '''
        
        if escolhido in lista_nomes:
            del[escolhido]
            print('Nome escolhido: ')
            print(lista_nomes)        
        
        print(f'O escolhido foi: {escolhido}') 
        lista_nomes.remove(escolhido)


        opcao = input('Deseja sortear outro nome? S - Sim / N - Não: ').lower()
        os.system('cls')
        
        if opcao != 's' :
            break 
        else:
            print('Não a nomes para ser sorteados')
            break
    print('Programa finalizado.')
    print(f'Os sorteados foram: {lista_sorteados}')

# importando lih 
from random import randint 

print('Tente adivinhar o numero! ')
num1 = int(input('Digite um numero :'))

num_secreto = randint(1, 2)

if num1 == num_secreto: 
    print('Parabens, voce acertou!')
else:
    print('Voce perdeu')
    print(f'Voce errou, o numero secreto era {num_secreto}.')

'''
versão 2.0
'''

# importando lih
import random 
import time
import os 
numero_secreto = random.randint(1, 100)

tentativas = 0
max_tentativas = 10
acertou = False 

print (30*"-", "Bem vindo ao AdivinheLogo", 30*"-")
print(f'Você tem {max_tentativas} tentativas para adivinhar o número secreto entre 1 e 100.')
print('Vamos começar?') 

while tentativas < max_tentativas:
    try: 
        #entrada do usuário
        palpite = int(input('Digite seu palpite: '))

    except:
        print('Por favor, digite um número válido.')
        continue
    tentativas += 1

    #verificar palpite 
    if palpite == numero_secreto:
        acertou = True
        break
    elif palpite < numero_secreto:
        print('Seu palpite foi muito baixo!.')
        time.sleep(1)
        os.system('cls')
        
    else:
        print('Seu palpite foi muito alto.')     
        time.sleep(1)
        os.system('cls')
       
if acertou: 
        print(f'Parabéns! Você acertou o número secreto {numero_secreto} em {tentativas} tentativas.')     
else:
        print(f'Que pena! Você não conseguiu o numerom secreto {numero_secreto} em {max_tentativas} tentativas.')
