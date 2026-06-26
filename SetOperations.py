IceCream_ingredients = {"Milk", "Chocolate", "Sugar"}
IceCream_ingredients.add("Vanila Essence")
print(IceCream_ingredients)
IceCream_ingredients.discard("Chocolate")
print(IceCream_ingredients)
Cake_Ingredients = {"Milk", "Eggs", "Sugar", "Vanila Essence", "Chocolate Icing"}
all_ingredients = IceCream_ingredients.union(Cake_Ingredients)
common = IceCream_ingredients.intersection(Cake_Ingredients)
print("All ingredients:", all_ingredients)
print("Common:", common)
