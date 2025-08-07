# Esse é o meu comentario

print (30*"-","COMEÇO DO MEU CÓDIGO",30*"-")
# comentario de linha

'''
comentario de bloco

'''

print (" ")
'''
# Meu nome
nome = "Henrique"
print ("Qual seu nome: ",nome)

# Minha idade
idade = 17 
print ("Qual sua idade: ",idade)

# Minha data de nascimento
data_de_nascimento = "12/11/2007"
print ("Qual sua data de nascimento: ",data_de_nascimento)

print (" ")

# Outra forma
nome = "Henrique"
idade = 17 
nascimento = "12/11/2007"
print ("Olá me chamo", nome, "tenho" , idade , "anos e nasci no dia", nascimento)

print (" ")

nome = "Henrique"
idade = 17
altura = 1.83
ativo = True

print ("O tipo de variavel nome é:", type(nome))
print ("O tipo de variavel nome é:", type(idade))
print ("O tipo de variavel nome é:", type(altura))
print ("O tipo de variavel nome é:", type(ativo))

print (" ")
print (30*"-", "OPERADORES",30*"-")
print (" ")

# operadores
num1 = 5
num2 = 2

soma = num1 + num2
divi = num1 / num2 #divisão comum
divisao_inteira = num1 // num2 #divisão inteira
mult = num1 * num2
expoente = num1 ** num2 
sub = num1 - num2
resto = num1 %2

print ("Resultado da soma: ",num1, "+", num2, "é", soma)
print ("Resultado da divisão: ",num1, "/", num2, "é", divi)
print ("Resultado da multiplicação: ",num1, "*", num2, "é", mult)
print ("Resultado da divisão inteira é: ",divisao_inteira)
print ("Resultado do expoente: ",expoente)
print ("Resultado da subtração: ",num1, "-", num2, "é", sub)
print ("resultado do resto de: ", num1, "é", resto )



print ()
print (30*"-", "OPERADORES DE COMPARAÇÃO",30*"-")
print ()

# operadores de comparação
num1 > num2 
num1 < num2 
num1 == num2
num1 >= num2
num1 <= num2
num1 != num2

ano = 2025
print ("ano atual",ano)
ano += 1
print ("ano acrecido",ano)
ano -= 1
print ("ano decrecido",ano)



print ()
print (30*"-", "ENTRADA DE DADOS",30*"-")
print ()

nome_usuario = input("Digite o seu nome: ")
print ("seja bem-vindo ao sistema python", nome_usuario)



print ()
print (30*"-", "CALCULADORA",30*"-")
print ()

num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero: "))

soma = num1 + num2
divi = num1 / num2 #divisão comum
divisao_inteira = num1 // num2 #divisão inteira
mult = num1 * num2
expoente = num1 ** num2 
sub = num1 - num2
resto = num1 %2

print ()
print ("Resultado dos calculos")
print ("Resultado da soma: ",num1, "+", num2, "é", soma)
print ("Resultado da divisão: ",num1, "/", num2, "é", divi)
print ("Resultado da multiplicação: ",num1, "*", num2, "é", mult)
print ("Resultado da divisão inteira é: ",divisao_inteira)
print ("Resultado do expoente: ",expoente)
print ("Resultado da subtração: ",num1, "-", num2, "é", sub)
print ("resultado do resto de: ", num1, "é", resto )
'''


print ()
print (30*"-", "CONVERTENDO TIPOS DE DADOS",30*"-")
print ()

ano_nascimento = input ("Digite seu ano de nascimento: ")
print(type(ano_nascimento))
# convertendo para inteiro
ano_nascimento = int(ano_nascimento)
print(type(ano_nascimento))

n1 = 10
n2 = 20
print ("A soma é:", n1+n2, type(n1), float(n2))

saudação = input("Digite seu nome: ")
cpf = input("Digite seu CPF:")
telefone = input ("Digite seu telefone:")

print(20*'-','Dados pessoais',20*'-')
print("Nome:", saudação)
print( 'Cpf:', cpf, '|Telefone:',telefone)
print(50* '-')