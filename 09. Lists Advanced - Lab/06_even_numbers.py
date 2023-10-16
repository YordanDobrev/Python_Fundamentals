def even_numbers(even):
    the_list = []
    index = 0
    for i in range(len(even)):
        if even[i] % 2 == 0:
            the_list.append(index)
        index += 1
    return the_list


# Read User Input
numbers = list(map(int, input().split(", ")))

# Logic
result = even_numbers(numbers)


# Print Output

print(result)
