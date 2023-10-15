def switch_letters(word):
    letters = list(word)
    letters[0], letters[-1] = letters[-1], letters[0]
    return ''.join(letters)


# Read User Input
words = input().split()
new_list = []

# Logic

for current_word in words:
    latest_word = ""
    rest_of_the_word = ""

    for current_letters in current_word:
        if current_letters.isdigit():
            latest_word += current_letters
            continue
        else:
            rest_of_the_word += current_letters

    final_word = chr(int(latest_word)) + switch_letters(rest_of_the_word)
    new_list.append(final_word)

# Print Output

print(*new_list)
