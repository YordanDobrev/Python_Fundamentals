pieces = int(input())
pianist = {}

for i in range(pieces):
    current_piece = input().split("|")
    piece = current_piece[0]
    composer = current_piece[1]
    key = current_piece[2]
    pianist[piece] = {composer: key}

command = input()

while command != "Stop":
    current_command = command.split("|")
    action = current_command[0]
    action_piece = current_command[1]

    if action == "Add":
        if action_piece in pianist.keys():
            print(f"{action_piece} is already in the collection!")
            command = input()
            continue
        else:
            pianist[action_piece] = {current_command[2]: current_command[3]}
            print(f"{action_piece} by {current_command[2]} in {current_command[3]} added to the collection!")

    elif action == "Remove":
        if action_piece in pianist.keys():
            pianist.pop(action_piece)
            print(f"Successfully removed {action_piece}!")
        else:
            print(f"Invalid operation! {action_piece} does not exist in the collection.")
            command = input()
            continue
    elif action == "ChangeKey":
        key_changed = False

        for current_key, current_value in pianist.items():
            if current_key == action_piece:
                for k, v in current_value.items():
                    current_value[k] = current_command[2]
                    print(f"Changed the key of {action_piece} to {current_command[2]}!")
                    key_changed = True
        if not key_changed:
            print(f"Invalid operation! {action_piece} does not exist in the collection.")

    command = input()

for key, value in pianist.items():
    for k, v in value.items():
        print(f"{key} -> Composer: {k}, Key: {v}")
