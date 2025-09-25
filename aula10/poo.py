import random
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
    def __init__(self,cavaleiro, nome, vida):
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
          print(f'{self.nome} atacou {personagem.nome} e tirou 30 pontos de vida, agora está com {personagem.vida}')
          print(f'Agora esta com {personagem.vida}')        
class Princesa(Personagem):
    def __init__(self, arco, nome, vida):
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

        
class GoblinComDardo(Personagem):
    def __init__(self, dardo, nome, vida):
        super().__init__(nome, vida)
        self.__dardo= dardo

    @property
    def dardo(self):
        return self.__dardo
    @dardo.setter
    def dardo(self, dardo):
        self.__dardo = dardo               
        
class BobEsponja:
    def __init__(self, nome, vida):
      super().__init__(nome, vida)

    def curar(self, personagem):
        dano = random.randint(30, 40)  
        personagem.vida -= dano
        print(f'{self.nome} curou {personagem.nome} e agora está com {personagem.vida} pontos de vida')
        print(f'A vida de {personagem.nome} agora é de {personagem.vida}')
    
personagem1 = Personagem('MegaCavaleiro', 2000)
print(f'Personagem: {personagem1.nome}')
print(f'Vida: {personagem1.vida}')

personagem2 = Personagem('Goblin com dardo', 500)
print(f'Personagem2: {personagem2.nome}')
print(f'Vida: {personagem2.vida}')
                                                                
personagem3 = Personagem('Princesa', 500)
print(f'Personagem3: {personagem3.nome}')
print(f'Vida: {personagem3.vida}')

personagem4 = Personagem('Bob Esponja',4000)
print(f'Personagem4: {personagem4.nome}')
print(f'Vida: {personagem4.vida}')




def atacar(self, personagem3):
    personagem3.vida -= 10
    print(f'{self.nome} atacou {personagem3.nome} e tirou 50 pontos de vida.')
    print(f'Agora esta com {personagem3.vida}')

def atacar(self, personagem):
    personagem.vida -= 20
    print(f'{self.nome} atacou {personagem.nome} e tirou 20 pontos de vida.')
    print(f'Agora esta com {personagem.vida}')

Mega_Cavaleiro = MegaCavaleiro('MEGA', 100)
Princesa_ = Princesa('PRINCESA', 100)
Goblin_ComDardo = GoblinComDardo('GOBLIN',100)
Bob_Esponja = BobEsponja('BOB', 100)

Mega_Cavaleiro.atacar(Bob_Esponja)
Bob_Esponja.curar(Bob_Esponja)
Princesa_.atacar(Goblin_ComDardo)
Bob_Esponja.curar(Goblin_ComDardo)



personagem4.atacar(personagem1)


'''
class Guerreiro(Personagem):
   def __init__(self, escudo, nome, vida):
    self._nome = nome
    self._vida = vida
    self._escudo = escudo


    def atacar(self, personagem):
          personagem.vida -= 40
          print(f'{self.nome} atacou {personagem.nome} e tirou 30 pontos de vida, agora está com {personagem.vida}')
          print(f'Agora esta com {personagem.vida}')

    def protecao(self):
        self.__vida += 10
'''