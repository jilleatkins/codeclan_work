# 1
ages = [5, 15, 64, 27, 84, 26]
odd_ages = [age for age in ages if age % 2 == 1]

print(odd_ages)

# 2
chicken_names = ["Hen Solo", "Cluck Norris", "Hennifer Lopez", "ChewPekka", "Feather Locklear"]
long_chicken_names = [chicken for chicken in chicken_names if len(chicken) >= 10]

print(long_chicken_names)

# 3
chicken_names = ["Hen Solo", "Cluck Norris", "Hennifer Lopez", "ChewPekka", "Feather Locklear"]
H_chicken_names = [chicken for chicken in chicken_names if chicken[0] == "H"]

print(H_chicken_names)

# 4
words = ["The", "quick", "brown", "fox", "jumped", "over", "the", "lazy", "dog"]
lower_letters = [letter[0].lower() for letter in words]

print(lower_letters)