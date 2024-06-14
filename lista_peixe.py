class Peixe:
    def __init__(self,especie,tipo_de_agua,profundidade_encontrada):
        self.especie = especie
        self.tipo_de_agua = tipo_de_agua
        self.profundidade_encontrada = profundidade_encontrada
    
    def __repr__(self):
        return f"peixe(especie='{self.especie}' , tipo de agua = {self.tipo_de_agua} , profundidade = {self.profundidade_encontrada})"

peixe1 = Peixe("baleia","salgada",122)
peixe2 = Peixe("golfinho","salgada",145)
peixe3 = Peixe("pinguim","salgada",23)
peixe4 = Peixe("tilapia","doce",34)
peixe5 = Peixe("leao marinho","salgada",578)

lista_peixes = [peixe1,peixe2,peixe3,peixe4,peixe5]

for peixe in lista_peixes:
    print(f"Escpecie: {peixe.especie}, Tipo de Agua: {peixe.tipo_de_agua}, profundidade: {peixe.profundidade_encontrada}")


