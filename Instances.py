class fruit:
    # class variable
    taste = "Sweet"

    # instance variable
    def __init__(self, name, color):
        self.name = name
        self.color = color
# Object Creation
apple = fruit("apple", "red")
mango = fruit("mango", "yellow")

print(apple.taste)
print(apple.name, apple.color)
print(mango.name,mango.color)
