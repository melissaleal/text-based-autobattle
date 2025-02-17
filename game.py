import random

class Character:
    def __init__(self, nome, classe, vida, ataqueMin, ataqueMax, defesaMin, defesaMax, dano, escudo, ult, arma):
        self.__nome = nome
        self.__classe = classe
        self.__vida = vida
        self.__ataqueMin = ataqueMin
        self.__ataqueMax = ataqueMax
        self.__dano = dano
        self.__defesaMin = defesaMin
        self.__defesaMax = defesaMax
        self.__escudo = escudo
        self.__ult = ult
        self.__arma = arma

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, value):
        self.__nome = value

    @property
    def classe(self):
        return self.__classe

    @classe.setter
    def classe(self, value):
        self.__classe = value

    @property
    def vida(self):
        return self.__vida

    @vida.setter
    def vida(self, value):
        self.__vida = value

    @property
    def ataqueMin(self):
        return self.__ataqueMin

    @ataqueMin.setter
    def ataqueMin(self, value):
        self.__ataqueMin = value

    @property
    def ataqueMax(self):
        return self.__ataqueMax

    @ataqueMax.setter
    def ataqueMax(self, value):
        self.__ataqueMax = value

    @property
    def dano(self):
        return self.__dano

    @dano.setter
    def dano(self, value):
        self.__dano = value

    @property
    def defesaMin(self):
        return self.__defesaMin

    @defesaMin.setter
    def defesaMin(self, value):
        self.__defesaMin = value

    @property
    def defesaMax(self):
        return self.__defesaMax

    @defesaMax.setter
    def defesaMax(self, value):
        self.__defesaMax = value

    @property
    def escudo(self):
        return self.__escudo

    @escudo.setter
    def escudo(self, value):
        self.__escudo = value

    @property
    def ult(self):
        return self.__ult
    
    @ult.setter
    def ult(self, value):
        self.__ult = value

    @property
    def arma(self):
        return self.__arma
    
    @arma.setter
    def arma(self, value):
        self.__arma = value

    def atacar(self, arma):
        return random.randint(self.__ataqueMin, self.__ataqueMax) + arma.danoExtra
        #return f"{self.__nome} ataca, causando {self.__dano} de dano!"

    def defender(self):
        return random.randint(self.__defesaMin, self.__defesaMax)
        #return f"{self.__nome} defende, criando um escudo de {self.__escudo}!"

    def estaVivo(self):
        if (self.__vida > 0):
            return 1
    
    def ultar(self):
        return "O personagem usou seu ataque especial"

class Warrior(Character):
    def __init__(self, nome, classe, vida, ataqueMin, ataqueMax, defesaMin, defesaMax, dano, escudo, ult, arma):
        super().__init__(nome, "Guerreiro", vida, ataqueMin, ataqueMax, defesaMin, defesaMax, dano, escudo, ult, arma)

    def ultar(self, arma):
        ataqueMin = self.ataqueMax
        return self.atacar(arma)

class Mage(Character):
    def __init__(self, nome, classe, vida, ataqueMin, ataqueMax, defesaMin, defesaMax, dano, escudo, ult, arma):
        super().__init__(nome, "Mago", vida, ataqueMin, ataqueMax, defesaMin, defesaMax, dano, escudo, ult, arma)

    def ultar(self, enemy, arma):
        escudo = 0
        return self.atacar(arma)

class Archer(Character):
    def __init__(self, nome, classe, vida, ataqueMin, ataqueMax, defesaMin, defesaMax, dano, escudo, ult, arma):
        super().__init__(nome, "Arqueiro", vida, ataqueMin, ataqueMax, defesaMin, defesaMax, dano, escudo, ult, arma)

    def ultar(self, enemy, arma):
        enemy.escudo(enemy.escudo() / 2)
        self.ataqueMin(self.ataqueMin() * 2)
        return self.atacar(arma)

class Weapon:
    def __init__(self, nome, danoExtra):
        self.__nome = nome
        self.__danoExtra = danoExtra

    @property
    def nome(self):
        return self.__nome
        
    @nome.setter
    def nome(self, value):
        self.__nome = value
        
    @property
    def danoExtra(self):
        return self.__danoExtra
        
    @danoExtra.setter
    def danoExtra(self, value):
        self.__danoExtra = value

arma1 = Weapon("Lâmina Lunar Crescente", 20)
arma2 = Weapon("Gadanho da Lua Nova", 10)
arma3 = Weapon("Cetro da Serpente Venenosa", 5)
arma4 = Weapon("Orbe da Medusa", 15)
meuPersonagem = Warrior("Diana", "Guerreiro", 200, 40, 50, 5, 15, 0, 0, "Colapso Minguante", arma2)
inimigo = Mage("Cassiopeia", "Mago", 200, 40, 50, 5, 15, 0, 0, "Olhar Petrificador", arma4)


while ((meuPersonagem.vida > 0) & (inimigo.vida > 0)):
    dano = meuPersonagem.atacar(meuPersonagem.arma)
    print(f"{meuPersonagem.nome} ataca, causando {dano} de dano!")
    escudo = inimigo.defender()
    print(f"{inimigo.nome} defende, criando um escudo de {escudo}!")
    if(escudo > dano):
        escudo = dano
    inimigo.vida = (inimigo.vida + escudo) - dano

    if (inimigo.estaVivo()):
        print(f"{inimigo.nome} sobreviveu, com {inimigo.vida}pts de vida!\n")
    else:
        print(f"{inimigo.nome} morreu.\n")
        break

    dano = inimigo.atacar(inimigo.arma)
    print(f"{inimigo.nome} ataca, causando {dano} de dano!")
    escudo = meuPersonagem.defender()
    print(f"{meuPersonagem.nome} defende, criando um escudo de  {escudo}!")
    if(escudo > dano):
        escudo = dano
    meuPersonagem.vida = (meuPersonagem.vida + escudo) - dano 

    if (meuPersonagem.estaVivo()):
        print(f"{meuPersonagem.nome} sobreviveu, com {meuPersonagem.vida}pts de vida!\n")
    else:
        print(f"{meuPersonagem.nome} morreu.\n")
        break

    escudo = inimigo.defender()
    print(f"{inimigo.nome} defende, criando um escudo de {escudo}!")
    ultimate = meuPersonagem.ultar(meuPersonagem.arma)
    print(f"{meuPersonagem.nome} ulta, causando {ultimate} de dano!")
    if(escudo > ultimate):
        escudo = ultimate
    inimigo.vida = (inimigo.vida + escudo) - ultimate 

    if (inimigo.estaVivo()):
        print(f"{inimigo.nome} sobreviveu, com {inimigo.vida}pts de vida!\n")
    else:
        print(f"{inimigo.nome} morreu.\n")
        break

    escudo = meuPersonagem.defender()
    print(f"{meuPersonagem.nome} defende, criando um escudo de {escudo}!")
    ultimate = inimigo.ultar(meuPersonagem, inimigo.arma)
    print(f"{inimigo.nome} ulta, causando {ultimate} de dano!")
    if(escudo > ultimate):
        escudo = ultimate
    meuPersonagem.vida = (meuPersonagem.vida + escudo) - ultimate

    if (meuPersonagem.estaVivo()):
        print(f"{meuPersonagem.nome} sobreviveu, com {meuPersonagem.vida}pts de vida!\n")
    else:
        print(f"{meuPersonagem.nome} morreu.\n")
        break
