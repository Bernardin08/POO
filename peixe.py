class Animal:
    def __init__(self, nome: str, tipo: str, idade: int):
        self.nome = nome
        self.tipo = tipo
        self.idade = idade

class Peixe(Animal):
    def __init__(self, nome: str, tipo: str, idade: int,habitat):
        super().__init__(nome, tipo=tipo, idade=idade)
        self.habitat = habitat
    
peixe = Peixe(nome="Nemo", tipo="Peixe", idade=76, habitat="agua")
print(f"Animal: {peixe.nome}, Tipo: {peixe.tipo}, Idade: {peixe.idade}, habitat : {peixe.habitat}")

