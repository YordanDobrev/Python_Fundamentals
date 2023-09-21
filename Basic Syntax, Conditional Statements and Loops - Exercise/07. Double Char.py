#Read User Input
command = input()

#Logic

while command != "End":

    word = ""
    for i in range(len(command)):
        current_index = command[i]
        word += current_index * 2

    if command != "SoftUni":
        print(word)
    command = input()


#Print Output