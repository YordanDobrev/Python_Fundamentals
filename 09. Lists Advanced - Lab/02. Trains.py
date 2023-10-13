# Read User Input
wagons = [0] * int(input())

# Logic

while True:
    command = input()
    command_split = command.split()

    if command == "End":
        break
    elif command_split[0] == "add":
        people = command_split[1]
        wagons[-1] += int(people)
    elif command_split[0] == "insert":
        index = command_split[1]
        people = command_split[2]
        wagons[int(index)] += int(people)
    elif command_split[0] == "leave":
        index = command_split[1]
        people = command_split[2]
        wagons[int(index)] -= int(people)

# Print Output

print(wagons)
