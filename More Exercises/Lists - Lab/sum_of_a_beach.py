# Read User Input
text_to_check = input().lower()

# Logic
counter = 0
beach_list = ["sand", "water", "fish", "sun"]

for i in range(len(beach_list)):
    if beach_list[i] in text_to_check:
        counter += text_to_check.count(beach_list[i])

# Print Output

print(counter)