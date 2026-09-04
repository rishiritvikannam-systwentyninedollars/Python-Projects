class Parrot:  # Class = It is a blueprint for defining something.
    species = ("Bird")

    def __init__(self, name, age): # __Init__ 
        self.name = name # Self Keyword = It is represents that it is a part of the class.
        self.age = age
        
    def sing(self, song):
        return "{} sings {}".format(self.name, song)
    
    def dance(self):
        return "{} is dancing".format(self.name)

Tom = Parrot("Tom", 5) # Object = It

print(Tom.sing("Happy"))
print(Tom.dance())