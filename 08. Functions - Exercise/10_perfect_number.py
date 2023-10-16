def perfect_number(some_num):
    divisor = 0

    for i in range(1, some_num):
        if some_num % i == 0:
            divisor += i

    if some_num == divisor:
        return "We have a perfect number!"
    return "It's not so perfect."


# Read User Input
num = int(input())

# Logic

result = perfect_number(num)

# Print Output

print(result)
