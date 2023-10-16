def revert(zero):
    digit_list = []

    for i in zero:
        if i != 0:
            digit_list.append(i)

    zero_list = [0]*abs(len(digit_list) - len(zero))
    final_list = digit_list + zero_list

    return final_list


# Read User Input
numbers = input().split(", ")

# Logic

converted_numbers = list(map(int, numbers))

# Print Output

print(revert(converted_numbers))