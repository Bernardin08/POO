class Ferrari:
    def motor_2000hp(self):
        return True

class Palio(Ferrari):
    def motor_2000hp(self):
        return False
    
ferrari = Ferrari()
print(ferrari.motor_2000hp())

palio = Palio()
print(palio.motor_2000hp())
