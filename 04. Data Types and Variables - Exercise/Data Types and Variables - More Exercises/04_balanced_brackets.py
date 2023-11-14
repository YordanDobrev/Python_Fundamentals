# Read User Input
lines = int(input())

# Logic
string = ""
balanced = False

for i in range(lines):
    current_symbol = input()
    if current_symbol == "(" or current_symbol == ")":
        string += current_symbol

for j in range(0, len(string), 2):
    if string[j] == "(" and string[j + 1] == ")":
        balanced = True
    else:
        balanced = False
        break

# Print Output

if balanced:
    print("BALANCED")
else:
    print("UNBALANCED")
