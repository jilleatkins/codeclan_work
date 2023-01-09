users = {
  "Jonathan": {
    "twitter": "jonnyt",
    "lottery_numbers": [6, 12, 49, 33, 45, 20],
    "home_town": "Stirling",
    "pets": [
    {
      "name": "fluffy",
      "species": "cat"
    },
    {
      "name": "fido",
      "species": "dog"
    },
    {
      "name": "spike",
      "species": "dog"
    }
  ]
  },
  "Erik": {
    "twitter": "eriksf",
    "lottery_numbers": [18, 34, 8, 11, 24],
    "home_town": "Linlithgow",
    "pets": [
    {
      "name": "nemo",
      "species": "fish"
    },
    {
      "name": "kevin",
      "species": "fish"
    },
    {
      "name": "spike",
      "species": "dog"
    },
    {
      "name": "rupert",
      "species": "parrot"
    },
    {
      "name": "fluffy",
      "species": "dog"
    }
  ]
  },
  "Avril": {
    "twitter": "bridgpally",
    "lottery_numbers": [12, 14, 33, 38, 9, 25],
    "home_town": "Dunbar",
    "pets": [
      {
        "name": "monty",
        "species": "snake"
      }
    ]
}


# 1. Get Jonathan's Twitter handle (i.e. the string `"jonnyt"`)
question1 =    {
    "name": "Jonathan", "Twitter handle": "jonnyt"
    },
for user in users:
    print(f'{user["name"]} is {user["twitter"]} on Twitter')

#ANSWER
# users["Jonathan"]["twitter"] 


# 2. Get Erik's hometown
question2 =    {
    "name": "Erik", "home_town": "Linlithgow"
    },
for user in users:
    print(f'{user["name"]} lives in {user["home_town"]}')


# ANSWER
#users["Erik"]["home_town"] 


# 3. Get the list of Erik's lottery numbers
question3 =    {
    "name": "Erik", "lottery_numbers": [18, 34, 8, 11, 24]
    },
for user in users:
    print(f'{user["name"]}s lottery numbers are {user["lottery_numbers"]}')

# ANSWER
#users["Erik"]["lottery_numbers"] 


# 4. Get the species of Avril's pet Monty
print(users["Avril"]["pets"][0]["species"])

# 5. Get the smallest of Erik's lottery numbers
Erik_lottery_numbers = [18, 34, 8, 11, 24]
s_num = min (Erik_lottery_numbers)
print ("The smallest of Erik's lottery numbers is", s_num)

#ANSWER
# sorted(users["Erik"]["lottery_numbers"][0])

# 6. Return an list of Avril's lottery numbers that are even
Avril_lottery_numbers = [12, 14, 33, 38, 9, 25]
num = 0
for num in Avril_lottery_numbers:
  if num % 2 == 0:
        print(num, end=" ")


# ANSWER
# even_numbers = []
# for number in users["Avril"]["lottery_numbers"]:
  # if number % 2 == 0:
        # even_numbers.append(number)
# print(even_numbers)


# 7. Erik is one lottery number short! Add the number `7` to be included in his lottery numbers
Erik_lottery_numbers.append(7)
print(Erik_lottery_numbers)

# ANSWER
# users["Erik"]["lottery_numbers"].append(7)

# 8. Change Erik's hometown to Edinburgh
users =    {
    "name": "Erik", "home_town": "Edinburgh"

    },
for user in users:
    print(f'{user["name"]} lives in {user["home_town"]}')

# ANSWER
# users["Erik"]["home_town"] = "Edinburgh"


# 9. Add a pet dog to Erik called "fluffy"

# ANSWER
# new_pet = {
#   "name": "fluffy",
#   "species": "dog"
# }
# users["Erik"]["pets"].append(new_pet)


# 10. Add another person to the users dictionary

#  },
#   "Nicola": {
#     "twitter": "drnic",
#     "lottery_numbers": [28, 17, 8, 9, 4, 11],
#     "home_town": "Gourock",
#     "pets": [
#       {
#         "name": "edie",
#         "species": "rabbit"
#      }
#    ]
#  }
# users["Erik"]["pets"].append(new_pet)