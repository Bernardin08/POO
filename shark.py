class Shark:
    animal_type = "fish"
    location = "ocean"
    followers = 0
    name = "juliao"

    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def set_followers(self, followers):
        self.followers = followers
        print("esse shark tem " + str(self.followers) + " seguidores")

    def set_name(self, name):
        self.name = name
        print(f"o nome dele do tubarao é {self.name}")

    def set_apga(self):
        self.animal_type = ""
        self.location = ""
        self.followers = 0
        self.age = 0
        self.name = ""
        print("tudo foi limpo")

new_shark = Shark("juliao",18)

print(new_shark.followers) #0
new_shark.set_followers(5)
print(new_shark.followers)

print(new_shark.name) #juliao
new_shark.set_name("filipao")
print(new_shark.name)

print(new_shark.name)
new_shark.set_apga()
print(new_shark.name)



    
