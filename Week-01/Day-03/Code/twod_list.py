# 2D list - These are the list of lists, commonly used to store data in a table-like format with rows and columns.
# Contains rows and columns data(a Table like format)
# countries = ["India", "US", "UK"]
# cities = ["Chennai", "Washington D.C.", "London"]
# locations = [countries, cities]


locations = [["India", "US", "UK"],   # countries
             ["Chennai", "Washington D.C.", "London"]  # cities
            ]
print(locations)
print(f"Popular Countries {locations[0]}")
print(f"I am Living in {locations[1][0]}, {locations[0][0]}.")  # Accessing India, Chennai

# looping through 2D list   
for location in locations:
    print(location)
    