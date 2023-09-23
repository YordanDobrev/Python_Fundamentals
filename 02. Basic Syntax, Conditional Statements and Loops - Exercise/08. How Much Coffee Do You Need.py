# Read User Input
command = input()

coffee = 0

# Logic

while command != "END":
    if command == "coding" or \
            command == "dog" or \
            command == "cat" or \
            command == "movie":
        coffee += 1
    elif command == "CODING" or \
            command == "DOG" or \
            command == "CAT" or \
            command == "MOVIE":
        coffee += 2
    command = input()

# Print Output

if coffee > 5:
    print(f"You need extra sleep")
else:
    print(coffee)
