class animal:
    def __init__(self, name, habitat):
        self.name = name
        self.habitat = habitat 

    def display(self):
        print("{self.name} | Habitat: {self.habitat}")

class Dog(animal):
    def __init__(self, name, habitat, breed):
        self.breed = breed