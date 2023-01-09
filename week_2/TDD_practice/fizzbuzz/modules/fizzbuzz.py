def fizzbuzz(num):
    if num % 5 ==0 and num % 3 ==0:
        return "Fizzbuzz" 
    if num % 3 == 0:
        return "Fizz"
    if num % 5 == 0:
        return "Buzz"
    return f"{num}"

# REFACTORING THIS CODE
def fizzbuzz(num):
    divisible_by_3 = num % 3 == 0
    divisible_by_5 = num % 5 == 0

    if divisible_by_3 and divisible_by_5:
        return "Fizzbuzz" 
    if divisible_by_3:
        return "Fizz"
    elif divisible_by_5:
        return "Buzz"
    else:
        return f"{num}"