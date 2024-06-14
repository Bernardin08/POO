#exemplo de uma lista
class Pessoa:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade
    
    def __repr__(self):
        return f"pessoa(nome='{self.nome}' , idade = {self.idade})"
    
pessoa1 = Pessoa("alice",15)
pessoa2 = Pessoa("pedro",20)
pessoa3 = Pessoa("torijo",18)

lista_pessoas = [pessoa1,pessoa2,pessoa3]

print(lista_pessoas)

for pessoa in lista_pessoas:
    print(f"Nome: {pessoa.nome}, Idade: {pessoa.idade}")

