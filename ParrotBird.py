class Parrot:
    species = ("Bird")

    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def sing(self, song):
        return "{} sings {}".format(self.name, song)
    
    def dance(self):
        return "{} is dancing".format(self.name)

Tom = Parrot("Tom", 5)

print(Tom.sing("Happy"))
print(Tom.dance())