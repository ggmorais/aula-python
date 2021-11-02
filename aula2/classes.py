class Animal:
    def __init__(self, comprimento, largura, specie):
        self.comprimento = comprimento
        self.largura = largura
        self.specie = specie

    def caracteristicas(self):
        print("Specie: ", self.specie)       
        print("Largura: ", self.largura)       
        print("Comprimento: ", self.comprimento)       

    def crescer(self, largura, comprimento):
        self.largura += largura
        self.comprimento += comprimento

    def andar(self):
        print("Andando...")

class Cachorro(Animal):
    def __init__(self, comprimento, largura):
        super().__init__(comprimento, largura, "Canino")

    def latir(self):
        print("Latindo...")




# gato = Animal(20, 50, "felino")
# gato.caracteristicas()

# leao = Animal(70, 40, "felino")
# leao.caracteristicas()

cachorro = Cachorro(20, 40)
cachorro.caracteristicas()
cachorro.crescer(30, 20)
print("\n")
cachorro.caracteristicas()

# animal.crescer(1, 30)
# print("\n")
# animal.caracteristicas()
# animal.andar()
