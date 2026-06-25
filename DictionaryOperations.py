# Creating The Dictionary
person={"name": "Rishi", "age" : 13, "grade" : 9}

# Accessing Values
print(person["name"]) 
print(person["age"])

# Printing the Dictionary
print(person)

# Safe access using .get()
print(person.get("grade"))
print(person.get("Birthplace", "N/A"))

#Update an existing value
person["age"] = 14

#Add a New Key-Value
person["Birthplace"] = "India"
print(person)

# Remove a specific key
person.pop("grade")
print(person)

#clear the entire dictionary
person.clear()
print(person)
