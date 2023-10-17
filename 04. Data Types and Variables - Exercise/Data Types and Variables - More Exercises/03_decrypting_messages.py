# Read User Input
key = int(input())
lines = int(input())

# Logic
word = ""

for i in range(lines):
    current_letter = chr(ord(input()) + key)
    word += current_letter

# Print Output

print(word)