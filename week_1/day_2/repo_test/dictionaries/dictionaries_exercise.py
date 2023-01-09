# Make a dictionary called avengers. It should contain keys for Iron Man and Hulk.

avengers = {"Iron Man", "Hulk"}
print(avengers)

# Each avenger is represented by another dictionary, and has a name 
# (Tony Stark and Bruce Banner respectively) and another dictionary 
# containing their attacks.

# Each attack should have an int value of the attack's 
# power. Iron man can punch (10) and kick (100) and Hulk can
#  smash (1000) and roll (500).

# Once you have created the dictionary, retrieve and print out
# the attack power of Hulks smash move.

avengers = {
    "Iron Man" : {
        "name" : "Tony Stark",
        "moves": {"Punch" : 10, 
                 "Kick" : 100}},
    "Hulk" : {
        "name" : "Bruce Banner",
        "moves": {"Smash" : 1000, "Roll" : 500}}
}
print(avengers)
print(avengers["Hulk"]["moves"]["Smash"])