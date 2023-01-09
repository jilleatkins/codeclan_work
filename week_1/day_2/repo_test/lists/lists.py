# create empty lists
empty_1 = []
empty_2 = list()
#you can use either of the above to create a list

# create a list with items
fruits = ["apple", "banana", "orange",]

# access by index
fruits[0]

# reassigning value at index
fruits[1] = 'plum'
# print(fruits)

# get the number of items
# num_of_fruits = len(fruits)
# print(num_of_fruits)

# remove last element
removed_fruit = fruits.pop()
print(f"I removed {removed_fruit}")

#  add a new fruit
fruits.append('pineapple')
print(fruits)

