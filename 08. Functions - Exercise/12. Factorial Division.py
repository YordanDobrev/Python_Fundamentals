def factorial(num):
    for i in range(1, num):
        num *= i
    return num


# Read User Input
first_num = int(input())
second_num = int(input())

# Logic

n1_factorial = factorial(first_num)
n2_factorial = factorial(second_num)

total = n1_factorial / n2_factorial

# Print Output

print(f"{total:.2f}")