def password_validator(word: str):
    list_to_print = []

    if len(word) < 6 or len(word) > 10:
        list_to_print.append("Password must be between 6 and 10 characters")

    if not word.isalnum():
        list_to_print.append("Password must consist only of letters and digits")

    digit_counter = 0
    for i in word:
        if i.isdigit():
            digit_counter += 1

    if digit_counter < 2:
        list_to_print.append("Password must have at least 2 digits")

    if not list_to_print:
        return "Password is valid"
    else:
        return "\n".join(list_to_print)


# Read User Input
password = input()

# Logic

result = password_validator(password)

# Print Output

print(result)
