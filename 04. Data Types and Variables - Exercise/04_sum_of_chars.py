#Read User Input
characters = int(input())

#Logic

total = 0

for i in range(characters):
    current_character = input()
    total += ord(current_character)

#Print Output

print(f"The sum equals: {total}")