# concatenação
# quebra de linha
# formatando decimais
# alterando virgula e ponto
# if else


#FIXME - contatenação com
nome = "Henrique"
idade = 17
altura = 1.83



print ('Olá meu nome é, ' + nome + ' , tenho ' + str (idade) + ' anos de idade')

#FIXME - concatenação com
print ('Olá, meu nome é,',nome,',tenho',idade, 'anos de idade')

#FIXME - concatenação com format
print('Olá, meu nome é,{},tenho  {}  anos de idade'. format (nome,idade))

#FIXME - concatenação com f-string
print(f'Olá, meu nome é {type(nome)}e tenho {idade+1} anos de idade')

#contatenação quebra de linha
print('O sabio sabia', end= '')
print('que sabio sabia assubiar')

valor = 1.23456789

# exebindo o valor com duas casa depois da virgula
print(f'{valor:.2f}')

print (50*"-")
peso = input('Digite seu peso').replace(',','.')
peso = float(peso)
print(f'{peso:.2f}'.replace(',','.'))


print (30*"-", "ATIVIDADES", 30*"-")

valor_str = "20"
valort_int = int(valor_str)
resultado = valort_int +10
print (resultado)


nome = input('Digite seu nome:')
idade = int(input('Digite sua idade:'))
            
print('Antes do if')
if idade >=18:
   print(f'Você é a maior de idade!')
   print('Você está dentro do bloco IF')
else:
   print(f'Você é menor de idade')
   print('Você está dentro do bloco ELSE')
   print ('Você está fora da estrtura condicional if else')


print (30*"-", "BOLETIM ESCOLAR",30*"-")
nome_aluno = input('Digite o nome do aluno: ')
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))
nota4 = float(input('Digite a quarta nota: '))

media = (nota1 + nota2 + nota3 + nota4) / 4

# se >= 7: aprovado
# se >= 5: recuperação
# reprovado

if media >=7:
   print(f'{nome_aluno}!|Aluno de Recuperação!')
   print(f'Nota 1: {nota1} | nota 2: {nota2}')
   print(f'Nota 1: {nota3} | nota 2: {nota4}')
   print(20*'-')
   print (f'média{media}')
elif media >=5:
   print(f'{nome_aluno}!|Aluno de Recuperação!')
   print(f'Nota 1: {nota1} | nota 2: {nota2}')
   print(f'Nota 1: {nota3} | nota 2: {nota4}')
   print(20*'-')
   print (f'média{media}')
else:
   print(f'{nome_aluno}!|Aluno de Recuperação!')
   print(f'Nota 1: {nota1} | nota 2: {nota2}')
   print(f'Nota 1: {nota3} | nota 2: {nota4}')
   print(20*'-')
   print (f'média{media}')



print (30*"-", "VARIAVEIS",30*"-")   
#variaveis
nome = input('Digite o seu nome:')
idade = int(input('Digite sua idade:'))
altura = float(input('Digite sua altura:'))

# verfica se o usuário possui os requisitos minimos
if idade >=12 and altura >= 1.2:
   print(f'A entrada de {nome} está autorizada.')
else: 
   print(f'A entrada de {nome} não está autorizada')