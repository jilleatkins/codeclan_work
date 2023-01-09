meal = ('yoghurt', 'roll', 'steak')
print(meal[0])

# my_first_empty_dictionary = {} - curly brackets automatically creates dictionary

# ALTERNATIVELY

# my_second_empty_dictionary = dict() - "dict()" is acting here as an alternative way to create a dictionary. It's working as a function.
# (This way is shit - don't use it)

meals = {"breakfast" : "yoghurt", "lunch": "roll", "dinner" : "steak"}
print(meals)

things = {1 : "2", "Jill" : True}
# Python doesn't mind you using different data types (e.g. strings, integers, etc.) in dictionaries
print(things)

# print(meals["breakfast"])
# print(meals["dinner"])
# print(things["Jill"][2])

# Lists must be ordered (hence use of indexes), whereas dictionaries don't have to be in order because they can be searched for by their tags - hence key-value pairs
# Dictionary elements cannot share the same tags with another - the last element will overwrite the previous element with the same tag

print("breakfast" in meals)
print("supper" in meals)

# Adding an element to a dictionary
meals ["supper"] = "pancakes"
print(meals)

# Removing an element from a dictionary
del(meals["breakfast"])
print(meals)

# Converts dictionary to a list. Keys are not lost - just not printed.
print(list(meals)) 

# OR, unconventionally
print(meals.keys())

# Returns list of values
print(meals.values())

# NESTING
countries = {
    "uk" : {"capital": "london", "population": 1000},
    "germany" : {"capital": "berlin", "population": 5000}
}

print(countries["germany"]["population"])


