def odd_even_finder(num):
    even_sum = 0
    odd_sum = 0

    for i in num:
        if int(i) % 2 == 0:
            even_sum += int(i)
        else:
            odd_sum += int(i)

    return odd_sum, even_sum


# Read User Input
number_to_use = input()

# Logic


sum_of_odd_digits, sum_of_even_digits = odd_even_finder(number_to_use)

# Print Output

print(f"Odd sum = {sum_of_odd_digits}, Even sum = {sum_of_even_digits}")
