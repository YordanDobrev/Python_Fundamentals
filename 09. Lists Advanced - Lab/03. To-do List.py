# Read User Input
notes = [0]*10

# Logic

while True:
    command = input()
    if command == "End":
        break

    tokens = command.split("-")
    priority = int(tokens[0]) -1
    note = tokens[1]
    notes.pop(priority)
    notes.insert(priority, note)

result = [element for element in notes if element != 0]
print(result)
# Print Output
