def characters(first_char, second_char):
    list_result = []

    for i in range(ord(first_char) + 1, ord(second_char)):
        list_result.append(chr(i))
    return list_result


# Read User Input

char_one = input()
char_two = input()

# Logic

result = " ".join(characters(char_one, char_two))

# Print Output

print(result)
