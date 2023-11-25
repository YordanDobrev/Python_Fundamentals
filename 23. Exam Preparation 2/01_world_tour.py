world_tour = input()
command = input()

while command != "Travel":
    current_command = command.split(":")
    action = current_command[0]

    if action == "Add Stop":
        index, string = int(current_command[1]), current_command[2]
        if index in range(len(world_tour)):
            world_tour = world_tour[:index] + string + world_tour[index:]

    elif action == "Remove Stop":
        start_index, end_index = int(current_command[1]), int(current_command[2])
        if start_index in range(len(world_tour)) and end_index in range(len(world_tour)):
            world_tour = world_tour[:start_index] + world_tour[end_index + 1:]

    elif action == "Switch":
        old_string, new_string = current_command[1], current_command[2]
        if old_string in world_tour:
            world_tour = world_tour.replace(old_string, new_string)

    print(world_tour)
    command = input()

print(f"Ready for world tour! Planned stops: {world_tour}")