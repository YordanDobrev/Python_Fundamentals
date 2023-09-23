#Read User Input
command = input()

#Logic

while command != "Welcome!":
    if command == "Voldemort":
        print(f"You must not speak of that name!")
        break
    elif len(command) < 5:
        print(f"{command} goes to Gryffindor.")
    elif len(command) == 5:
        print(f"{command} goes to Slytherin.")
    elif len(command) == 6:
        print(f"{command} goes to Ravenclaw.")
    elif len(command) > 6:
        print(f"{command} goes to Hufflepuff.")

    command = input()

#Print Output
if command == "Welcome!":
    print(f"Welcome to Hogwarts.")