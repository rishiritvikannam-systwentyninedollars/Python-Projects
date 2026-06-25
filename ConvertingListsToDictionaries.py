# two related lists
placements = [1, 2, 3, 4, 5]
Countries = ["Portugal", "Spain", "Argentina", "France", "Brazil"]

# Convert to a Dictionary using zip()
teams = dict(zip(placements, Countries))
print(teams)

#Look Up a Team By Its Placement
print(teams[3])