class Shark():
    def nadar(self):
        print("o tubarao esta nadando")
    
    def nadar_pra_tras(self):
        print("o tubarao nao consegue nadar pra tras, mas pode afundar pra tras")

    def skeleton(self):
        print("o esqueleto do tubarao é feito de cartilagem.")

class Clownfish():
    def nadar(self):
        print("o peixe-palhaço esta nadando")

    def nadar_pra_tras(self):
        print("o peixe-palhaço pode nadar pra tras")

    def skeleton(self):
        print("o esqueleto do peixe-palhaço é feito de osso")

shark = Shark()
clownfish = Clownfish()

for peixe in (shark,clownfish):
    peixe.nadar()
    peixe.nadar_pra_tras()
    peixe.skeleton()
