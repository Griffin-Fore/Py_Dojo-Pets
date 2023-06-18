import Pet

class Ninja:
    def __init__(self,first_name,last_name,treats,pet_food,pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet

    def walk(self):
        self.pet.play()
        return self
    
    def feed(self):
        self.pet.eat()
        return self
    
    def bathe(self):
        self.pet.noise()
        print(f"{self.first_name} bathed {self.pet.name}")
        return self

#create a new
riley = Pet.Pet("riley","dog",["sit","stand","play_dead"])
marco = Pet.Cat("marco")

#pass in the pet instance by name
john = Ninja("John","Reilly","Snausages","Beneful",riley)

mark = Ninja("Markus","Person","Catnip","Fancy Feast",marco)

john.walk()
john.feed()
john.bathe()

mark.walk()
mark.feed()
mark.bathe()