users = {}

command = input()


while command != "Lumpawaroo":

    if "|" in command:
        current_command = command.split(" | ")
        force_side = current_command[0]
        force_user = current_command[1]

        if force_side not in users.keys():
            users[force_side] = []
            users[force_side].append(force_user)
        else:
            continue

    elif "->" in command:
        current_command = command.split(" -> ")
        user = current_command[0]
        side = current_command[1]

        if user in users.values():
            users[side].append(user)
        elif user not in users.values():
            pass


    command = input()

print(users)