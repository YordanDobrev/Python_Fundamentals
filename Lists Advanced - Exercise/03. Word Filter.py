# Read User Input
word = input().split()

# Logic

new_layout = [text for text in word if len(text) % 2 == 0]

# Print Output

print("\n".join(new_layout))