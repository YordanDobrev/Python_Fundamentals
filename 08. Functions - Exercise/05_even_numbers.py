def even_num(the_list: list):
    new_list = []

    for i in range(len(the_list)):
        if int(the_list[i]) % 2 == 0:
            new_list.append(int(the_list[i]))

    return new_list


# Read User Input
list_to_use = input().split()

# Logic


# Print Output

print(even_num(list_to_use))
