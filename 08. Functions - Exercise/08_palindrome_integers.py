def palindrome(some_number: str) -> bool:
    if some_number == some_number[::-1]:
        return True
    return False


# Read User Input
numbers = input().split(", ")

# Logic

# Print Output
for number in numbers:
    print(palindrome(number))
