def convert_digit(the_list):
    new_list = []
    for i in the_list:
        new_list.append(int(i))
    return new_list


# Read User Input
list_to_use = input().split()

# Logic

result = sorted(convert_digit(list_to_use))

# Print Output

print(result)
