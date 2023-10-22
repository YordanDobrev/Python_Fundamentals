# Read User Input
shelf = input().split("&")
command = input()

# Logic

while True:
    if command == "Done":
        break

    command = command.split(" | ")

    if command[0] == "Add Book":
        if command[1] not in shelf:
            shelf.insert(0, command[1])

    if command[0] == "Take Book":
        if command[1] in shelf:
            shelf.remove(command[1])

    if command[0] == "Swap Books":
        if command[1] in shelf and command[2] in shelf:
            a, b = shelf.index(command[1]), shelf.index(command[2])
            shelf[a], shelf[b] = shelf[b], shelf[a]

    if command[0] == "Insert Book":
        if command[1] not in shelf:
            shelf.append(command[1])

    if command[0] == "Check Book":
        if int(command[1]) > len(shelf) or int(command[1]) < len(shelf):
            print(shelf[int(command[1])])

    command = input()

# Print Output

print(", ".join(shelf))
