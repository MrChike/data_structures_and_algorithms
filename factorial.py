def factorial(number):
    count = number
    total = number
    
    while count != 1:
        total *= count - 1
        count -= 1

        return total


print(factorial(5))
