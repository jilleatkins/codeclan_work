# NORMAL WAY

numbers = range(1, 11)
evens_squared = []

for number in numbers:
    if number % 2 == 0:
        evens_squared.append(number * number)

# print(evens_squared)

# LIST COMPREHENSION

# PSEUDOCODE: evens_squared = [expression for item in list if condition]

numbers = range(1, 11)
evens_squared = [number * number for number in numbers if number % 2 == 0]
# (number * number is WHAT WE'RE TRYING TO DO, and only happens if (number % 2 == 0) is TRUE)
# this is a FOR LOOP is one line (like Larry does)

print(evens_squared)