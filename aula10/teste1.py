import random
import time
class Personagem:
    #construtor
    def __init__(self, nome, vida):
        # encapsulamento
        self.__nome = nome
        self.__vida = vida
     # defininfdo GET
    @property
    def nome(self):
        return self.__nome
    
    #definindo SET
    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome
    
    @property
    def vida (self):
        return self.__vida
    
    @vida.setter
    def vida(self, vida):
        self.__vida = vida   
class MegaCavaleiro(Personagem):
    def __init__(self, nome, vida, cavaleiro):
        super().__init__(nome, vida)
        self.__cavaleiro = cavaleiro

    @property
    def cavaleiro(self):
        return self.__cavaleiro

    @cavaleiro.setter
    def cavaleiro(self, cavaleiro):
        self.__cavaleiro = cavaleiro

    def atacar(self, personagem):
        dano = random.randint(80, 90)
        personagem.vida -= dano
        print(f'{self.nome} atacou {personagem.nome} e tirou {dano} pontos de vida, agora está com {personagem.vida}')
        print()
class Princesa(Personagem):
    def __init__(self, nome, vida, arco):
        super().__init__(nome, vida)
        self.__arco = arco

    @property
    def arco(self):
        return self.__arco

    @arco.setter
    def arco(self, arco):
        self.__arco = arco

    def atacar(self, personagem):
        dano = random.randint(10, 30)
        personagem.vida -= dano
        print(f'{self.nome} atacou {personagem.nome} e causou {dano} de dano. {personagem.nome} agora tem {personagem.vida} de vida.')
        print()
class GoblinComDardo(Personagem):
    def __init__(self, nome, vida, dardo):
        super().__init__(nome, vida)
        self.__dardo = dardo

    @property
    def dardo(self):
        return self.__dardo

    @dardo.setter
    def dardo(self, dardo):
        self.__dardo = dardo

    def atacar(self, personagem):
        dano = random.randint(5, 15)
        personagem.vida -= dano
        print(f'{self.nome} atacou {personagem.nome} e causou {dano} de dano. {personagem.nome} agora tem {personagem.vida} de vida.')
        print()
class BobEsponja(Personagem):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)

    def atacar(self, personagem):
        dano = random.randint(80, 90)
        personagem.vida += dano 
        print(f'{self.nome} atacou {personagem.nome} e causou {dano} de dano. {personagem.nome} agora tem {personagem.vida} de vida.')
        print()
print('------- PERSONAGENS -------')
limpar_tela = '\n' * 100

personagem1 = Personagem('MegaCavaleiro', 500)
print(f'Personagem: {personagem1.nome}')
print(f'Vida: {personagem1.vida}')
print()
personagem2 = Personagem('Goblin com dardo', 100)
print(f'Personagem2: {personagem2.nome}')
print(f'Vida: {personagem2.vida}')
print()                                                                
personagem3 = Personagem('Princesa', 100)
print(f'Personagem3: {personagem3.nome}')
print(f'Vida: {personagem3.vida}')
print()
personagem4 = Personagem('BobEsponja', 800)
print(f'Personagem3: {personagem4.nome}')
print(f'Vida: {personagem4.vida}')

#Agora com os personagens criados, vamos iniciar uma batalha entre eles mostrando a tela separada e o inicio da batalha



Mega_Cavaleiro = MegaCavaleiro('MegaCavaleiro', 2000, 'Socos')
Princesa_ = Princesa('Princesa', 50, 'Arco')
Goblin_ComDardo = GoblinComDardo('Goblin com dardo', 500, 'Dardo')
Bob_Esponja = BobEsponja('Bob Esponja', 4000)

#agora fazer outra tela apos pressionar enter
input('Pressione Enter para iniciar a batalha...')
print(limpar_tela)
print('------- BATALHA -------')

#Organizar a batalha em turnos pra ficar mais interessante trocando os combates, até ter um vencedor, anunciando os perdedores em cada turno
while personagem1.vida > 0 and personagem2.vida > 0 and personagem3.vida > 0 and personagem4.vida > 0:
    Mega_Cavaleiro.atacar(Princesa_)
    if Princesa_.vida <= 0:
        print(f'{Princesa_.nome} foi derrotada!')
        break
    time.sleep(1)
    Princesa_.atacar(Goblin_ComDardo)
    if Goblin_ComDardo.vida <= 0:
        print(f'{Goblin_ComDardo.nome} foi derrotado!')
        break
    time.sleep(1)
    Goblin_ComDardo.atacar(Bob_Esponja)
    if Bob_Esponja.vida <= 0:
        print(f'{Bob_Esponja.nome} foi derrotado!')
        break
    time.sleep(1)
    Bob_Esponja.atacar(Mega_Cavaleiro)
    if Mega_Cavaleiro.vida <= 0:
        print(f'{Mega_Cavaleiro.nome} foi derrotado!')
        break
    time.sleep(1)
    input('Pressione Enter para o próximo turno...')
#faça ataques aleatorios entre os personagens até que um deles tenha sua vida reduzida a zero ou menos ate vencer
    print(limpar_tela)
    time.sleep(1)
print('------- FIM DA BATALHA -------')
print('Batalha encerrada!')
print(f'Vida final de {Mega_Cavaleiro.nome}: {Mega_Cavaleiro.vida}')
print(f'Vida final de {Princesa_.nome}: {Princesa_.vida}')
print(f'Vida final de {Goblin_ComDardo.nome}: {Goblin_ComDardo.vida}')
print(f'Vida final de {Bob_Esponja.nome}: {Bob_Esponja.vida}')
#apresentar o vencedor
if Mega_Cavaleiro.vida > 0:
    print(f'O vencedor é {Mega_Cavaleiro.nome}!')
elif Princesa_.vida > 0:
    print(f'O vencedor é {Princesa_.nome}!')
elif Goblin_ComDardo.vida > 0:
    print(f'O vencedor é {Goblin_ComDardo.nome}!')
elif Bob_Esponja.vida > 0:
    print(f'O vencedor é {Bob_Esponja.nome}!')
else:
    print('Todos foram derrotados!')