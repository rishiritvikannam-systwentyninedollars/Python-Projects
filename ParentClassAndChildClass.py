class Animal:              #Parent class
    def display(self):
        print("I am an Animal.")

class Dog(Animal):         #Child Class - inherits from Animal
    pass

d = Dog()
d.display() 

    