# Defined with curved parenthesis (preferred; neater)
car = ('Ford', 'Escort', 1300, 'Red')

# Defined without parentheses (floating elements; not so neat)
car_2 = 'Ford', 'Escort', 1300, 'Red'

print(car)
print(type(car))
print(car_2)

# Defining an empty tuple

# Method 1
empty_tuple = ()

# OR

# Method 2
empty_tuple_2 = tuple()

# Accessing value by index
model = car[1]
colour = [-1]
print(f'Model: {model} Colour: {colour}')

# Can't modify tuples - they are immutable
# car[1] = 'Focus'

# Count tuple elements
tuple_count = len(car)
print(tuple_count)

fruits = ('banana', 'banana', 'orange')
print(fruits.count('banana'))
print(car.count(1300))

# Tuple containing only single element must be followed by a "trailing"/"oxford" comma
# single_tuple = ('Jill')
# print(type(single_tuple))

