# Read User Input
pirate_ship = input().split(">")
warship_ship = input().split(">")
max_health = int(input())
command = input()
pirate_ship_sunk = False
warship_ship_sunk = False
# Logic
while True:
    if command == "Retire":
        break
    command = command.split()
    if command[0] == "Fire":
        index1 = int(command[1])
        index2 = int(command[2])
        if index1 < 0 or index1 > len(warship_ship):
            command = input()
            continue
        current_section_to_attack = warship_ship[index1]
        dmg_done = int(current_section_to_attack) - index2
        if dmg_done >= int(current_section_to_attack):
            warship_ship_sunk = True
            break
        warship_ship.pop(index1)
        warship_ship.insert(index1, str(dmg_done))

    elif command[0] == "Defend":
        damage = int(command[3])

        for i in range(int(command[1]), int(command[2])+1):
            if i > len(pirate_ship) - 1:
                break
            current_section = pirate_ship[i]
            current_dmg_done = int(current_section) - damage
            if current_dmg_done >= int(current_section):
                pirate_ship_sunk = True
                break
            pirate_ship.pop(i)
            pirate_ship.insert(i, str(current_dmg_done))

    elif command[0] == "Repair":
        if int(command[1]) < 0 or int(command[1]) > len(pirate_ship):
            command = input()
            continue

        health = int(command[2])
        section_health = pirate_ship[int(command[1])]

        if health + int(section_health) > max_health:
            pirate_ship.pop(int(command[1]))
            pirate_ship.insert(int(command[1]), str(max_health))
        else:
            current_section = int(command[1])
            pirate_section = pirate_ship[current_section]
            current_health_done = int(pirate_section) + int(health)
            pirate_ship.pop(int(command[1]))
            pirate_ship.insert(int(command[1]), str(current_health_done))

    elif command[0] == "Status":
        status = [int(count) for count in pirate_ship if int(count) < (max_health * 0.2)]
        print(f"{status} sections need repair.")
    command = input()

pirate_ship_status = sum(status)
warship_ship_status = sum(map(int,warship_ship))

# Print Output

if pirate_ship_sunk:
    print("You lost! The pirate ship has sunken.")
elif warship_ship_sunk:
    print("You won! The enemy ship has sunken.")
else:
    print(f"Pirate ship status: {pirate_ship_status}\n"
          f"Warship status: {warship_ship_status}")
