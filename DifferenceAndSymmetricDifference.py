IceCream = {"Vanila Essence", "Milk", "Sugar"}
Cake = {"Milk", "Eggs", "Sugar", "Chocolate powder", "Chocolate Icing"}

only_IceCream = IceCream.difference("Cake")
unique_to_each = IceCream.symmetric_difference("Cake")
print("Only in IceCream:", only_IceCream)
print("Not Shared:", unique_to_each )