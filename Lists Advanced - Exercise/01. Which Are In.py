import re

# Read User Input
first_string = input().split(", ")
second_string = input().split(", ")

substrings = []
# Logic

for i in first_string:
    for j in second_string:
        if i in j:
            substrings.append(i)
            break

# Print Output

print(substrings)