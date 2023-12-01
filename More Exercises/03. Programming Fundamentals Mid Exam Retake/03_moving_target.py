targets = input().split()
command = input()

while command != "End":
    current_command = command.split()
    action = current_command[0]
    index = int(current_command[1])

    if action == "Shoot":
        power = int(current_command[2])
        if 0 <= index <= len(targets):
            targets[index] = str(int(targets[index]) - power)
            if int(targets[index]) <= 0:
                targets.pop(index)

    elif action == "Add":
        value = int(current_command[2])
        if 0 <= index <= len(targets):
            targets.insert(index, str(value))
        else:
            print("Invalid placement!")

    elif action == "Strike":
        radius = int(current_command[2])
        left_part = index - radius
        right_part = index + radius
        if left_part >= 0 and right_part <= len(targets):
            targets = targets[:left_part] + targets[right_part + 1::]
        else:
            print("Strike missed!")

    command = input()

print("|".join(targets))
