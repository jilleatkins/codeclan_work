# FUNCTIONS
# What is a function?

# Why use functions?
# Organisation
# Reusability
# Modularity

# How to create functions

# How to run functions

# How to get a value

# Parameters and arguments

# Scope

# GREETINGS WITH SINGLE AND MULTIPLE PARAMETERS
# def greet(name, time_of_day):
#     return "Good " + time_of_day + ", " +name + "!"

# Single parameter
# greeting = greet("Ash", "morning")
# print(greeting)

# Multiple parameters
# name_1 = "Ash"
# time_of_day_1 = "morning"
# greeting = greet(name_1, time_of_day_1)
# print(greeting)

# name_2 = "Ben"
# time_of_day_2 = "afternoon"
# greeting = greet(name_2, time_of_day_2)
# print(greeting)


# GREETINGS
# def greet():
#     words = "Hey!"
#     return words

# def greet_two():
#     words = "Hey!"
#     return words
# print(greet_two())

# CHICKENS
# chickens = [
#   { "name": "Margaret", "age": 2, "eggs": 0 },
#   { "name": "Hetty", "age": 1, "eggs": 2 },
#   { "name": "Henrietta", "age": 3, "eggs": 1 },
#   { "name": "Audrey", "age": 2, "eggs": 0 },
#   { "name": "Mabel", "age": 5, "eggs": 1 },
# ]

# def count_eggs(list):

#     total_eggs = 0

#     for bird in list:
#         total_eggs += bird["eggs"]
#         bird["eggs"] = 0 # eggs have been collected
#     return (f"{total_eggs} eggs collected")
# print(count_eggs(chickens))


# chickens = [
#   { "name": "Margaret", "age": 2, "eggs": 0 },
#   { "name": "Hetty", "age": 1, "eggs": 2 },
#   { "name": "Henrietta", "age": 3, "eggs": 1 },
#   { "name": "Audrey", "age": 2, "eggs": 0 },
#   { "name": "Mabel", "age": 5, "eggs": 1 },
# ]

# def find_chicken_by_name(chicken_list, chicken_name):
#     for chicken in chicken_list:
#         if chicken["name"] == chicken_name:
#             return chicken

#     return found_chicken

# chicken = find_chicken_by_name(chickens, "Margaret")
# print(chicken)

# EXERCISE: Write a function that can find a user in the list by user_id
users = [
  { "user_id": 1, "first_name": "Guido", "last_name": "van Rossum" },
  { "user_id": 2, "first_name": "Katherine", "last_name": "Johnson" },
  { "user_id": 3, "first_name": "Dorothy", "last_name": "Vaughan" },
  { "user_id": 4, "first_name": "Hen", "last_name": "Solo" },
  { "user_id": 5, "first_name": "Mary", "last_name": "Jackson" },
]

def find_user_by_id(user_list, user_id):
    for user in user_list:
        if user["user_id"] == user_id:
            return user

    return None

desired_id = input("Please enter the desired user ID: ")
desired_id = int(desired_id)
user = find_user_by_id(users, desired_id)
print(user)

# UNIT TESTING
