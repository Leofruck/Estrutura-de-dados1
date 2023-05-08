from Computador import Computador

class Notebook(Computador):
    def __init__(self, modelo, cor, preco, tempoDeBateria):
        super().__init__(modelo, cor, preco)
        self.__tempoDeBateria = tempoDeBateria
    
    def getInformacoes(self):
        return f"Modelo: {self.modelo}, Cor: {self.cor}, Preço: R${self.preco:.2f}, Tempo de Bateria: {self.__tempoDeBateria} horas"
    
    def cadastrar(self):
        print("Cadastro de Notebook realizado com sucesso!")