class Computador:
    def __init__(self, cpu: str, qntd_memoria: int, ligado: bool):
        self.cpu = cpu
        self.qntd_memoria = qntd_memoria
        self.ligado = ligado
    
    def ligar(self):
        self.ligado = True
        print("o seu PC está ligado!")
    
    def desligar(self):
        self.ligado = False
        print("Seu pc está desligado!")

class Pc_gamer(Computador):
    def __init__(self, cpu: str, qntd_memoria: int, ligado: bool, jogando: bool):
        super().__init__(cpu, qntd_memoria, ligado)
        self.jogando = jogando
    
    def iniciar_jogo(self):
        self.jogando = True
        print("Você esta jogando")
    
    def fechar_jogo(self):
        self.jogando = False
        print("Voce nao esta jogando")
    
pc = Pc_gamer(cpu = "ryzen 5", qntd_memoria = "16gb", ligado = True, jogando = False)
pc.ligar()
pc.desligar()
pc.iniciar_jogo()
pc.fechar_jogo()

    