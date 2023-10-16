def calculations(the_list):
    new_list = []
    for i in the_list:
        new_list.append(int(i))

    max_num = max(new_list)
    min_num = min(new_list)
    sum_of_all = sum(new_list)

    return min_num, max_num, sum_of_all


# Read User Input
the_list_to_use = input().split()

# Logic

minimum_number, maximum_number, sum_of_all_numbers = calculations(the_list_to_use)

# Print Output

print(f"The minimum number is {minimum_number}")
print(f"The maximum number is {maximum_number}")
print(f"The sum number is: {sum_of_all_numbers}")