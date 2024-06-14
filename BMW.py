class Carro:
    def __init__(self,marca,modelo,ano,combustivel,km):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.combustivel = combustivel
        self.km = km

carro = Carro("BMW","XDRIVE40",2022,"elétrico",17.249)

print(carro.marca,carro.modelo,carro.ano,carro.combustivel,carro.km)
