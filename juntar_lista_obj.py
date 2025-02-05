#exemplo de juntar duas listas e formar uma lista de objetos
class Pessoa:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade
    
    def __repr__(self):
        return f"pessoa(nome='{self.nome}' , idade = {self.idade})"

lista_pessoas = []

nomes = ["alice","bob","carlos"]
idades = [30,25,40]

for nome, idade in zip(nomes, idades):
    lista_pessoas.append(Pessoa(nome,idade))

print(lista_pessoas)