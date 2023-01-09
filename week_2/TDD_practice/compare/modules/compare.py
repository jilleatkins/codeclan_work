def compare(user_input, computer_input):
    if user_input > computer_input:
        return f"{user_input} is greater than my number"
    if user_input < computer_input:
        return f"{user_input} is less than my number"
    if user_input == computer_input:
        return f"{user_input} is equal to my number"