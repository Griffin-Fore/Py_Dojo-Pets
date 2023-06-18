class Pet:
    def __init__(self, pet_name, pet_type, tricks):
        self.name = pet_name
        self.pet_type = pet_type
        self.tricks = tricks
        self.health = 100
        self.energy = 100

    def sleep(self):
        self.energy += 25

    def eat(self):
        self.energy += 5
        self.health += 10
        print(f"{self.name} ate, {self.health} health.")

    def play(self):
        self.health += 5
        print(f"{self.name} played", self.health)

    def noise(self):
        print("Mrrp!")

class Cat(Pet):
    def __init__(self, pet_name):
        self.name = pet_name
        self.pet_type = "cat"
        self.tricks = None
        self.health = 50
        self.energy = 1000
