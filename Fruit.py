# Class = Class is a blueprint for for creating objects. It defines Attribrutes and Methods.
# Object = An Object can be defined as a class instance and they hold atribrutes and behaviors.
# Methods = Methods define the behavior of an object. They are functions that are defined inside a class.
# __init__Method = They are used to assign values to object attribrutes at the time of object creation. It is automatically called every time the object is created for a class. 
class fruit:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    # instance method
    def intro(self):
        print("Hello, My Name is", self.name)

# Creating An Object
banana = fruit("banana", "Yellow")
coconut = fruit("coconut", "Green")

# Calling the function
banana.intro()
coconut.intro()
