def pal_func(pal_indrome):
    the_list = []

    for word in pal_indrome:
        if word == "".join(reversed(word)):
            the_list.append(word)
    return the_list


# Read User Input
palindrome = input().split()
word_to_check = input()

# Logic


# Print Output

print(pal_func(palindrome))
print(f"Found palindrome {pal_func(palindrome).count(word_to_check)} times")