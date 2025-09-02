#Atividade numero 7 - Solicite dois números e verifique se o segundo é menor que o primeiro.
num1 = float(input('Escreva o primeiro numero: '))
num2 = float(input('Escreva o segundo numero: '))

if num1 < num2 : input(f'O segundo numero é maior que o primeiro numero ')

if num1 > num2 : input(f'O segundo numero não é maior que o primeiro numero ')


#Ativida numero 8 - troca de nomes e sobrenomes
print(30*"-","RESPONDA AS QUESTÕES SOBRE VOCÊ ABAIXO",30*"-")

nome1 = input('Nome da primeira pessoa: ')
sobrenome1 = input('Sobrenome da primeira pessoa: ')

nome2 = input('Nome da segunda pessoa: ')
sobrenome2 = input('Sobrenome da segunda pessoa: ')

print(f' Nome da primeira pessoa com o sobrenome da segunda pessoa: {nome1} {sobrenome2}')
print(f' Nome da segunda pessoa com o sobrenome da primeira pessoa: {nome2} {sobrenome1}')

#Atividade numero 9 - Peça um número e exiba a metade dele.
print(13*"-",'Digite um número e veja a metade dele abaixo',13*"-")

numero = float(input('Digite um número: '))
metade = numero / 2
print(f'A metade de {numero} é {metade}')

# Atividade numero 10 - Solicite a altura e a largura de um retângulo e exiba a área.
print(10*"-","CÁLCULO DA ÁREA DE UM RETÂNGULO",10*"-")
altura = float(input('Digite a altura do retângulo: '))
largura = float(input('Digite a largura do retângulo: '))
area = altura * largura
print(f'O resultado da área do retângulo é {area}')

#Atividade numero 11 - Crie um sistema que receba um número e exiba o seu antecessor e o seu sucessor.
print(10*"-","ANTECESSOR E SUCESSOR",10*"-")
numero = int(input('Digite um numero aleatório a seguir: '))
sucessor = numero + 1
antecessor = numero - 1
print(f'O sucessor do nuemro digitado é {sucessor}')
print(f'O antecessor do numero digitado é {antecessor}')

#Atividade numero 12 - Crie um sistema que receba um número e mostre o seu dobro, triplo, e raiz
print(10*"-","SISTEMA QUE MOSTRA O DOBRO, TRIPLO E RAIZ QUADRADA",10*"-")
numero = int(input('Digite o numero:'))
dobro = numero * 2
triplo = numero * 3
raiz_quadrada = numero ** 0.5

print(f'O dobro do seu {numero} é: {dobro}')
print(f'O triplo do seu {numero} é: {triplo}')
print(f'O dobro do seu {numero} é: {raiz_quadrada}')
