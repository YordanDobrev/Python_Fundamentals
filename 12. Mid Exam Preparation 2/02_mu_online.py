# Read User Input
rooms = input().split("|")

# Logic

health = 100
bitcoins = 0
best_room = 0
killed = False
current_index = 0

while True:
    best_room += 1
    current_room = rooms[current_index].split()

    command = current_room[0]
    number = int(current_room[1])

    if command == "potion":
        temp_health = health
        health += number
        if health > 100:
            health = 100
        difference = health - temp_health
        print(f"You healed for {difference} hp.")
        print(f"Current health: {health} hp.")

    elif command == "chest":
        bitcoins += number
        print(f"You found {number} bitcoins.")

    else:
        if health - number <= 0:
            killed = True
            break
        else:
            health -= number
            print(f"You slayed {command}.")

    current_index += 1

    if len(rooms) == current_index:
        break

# Print Output

if killed:
    print(f"You died! Killed by {command}.")
    print(f"Best room: {best_room}")
else:
    print(f"You've made it!")
    print(f"Bitcoins: {bitcoins}")
    print(f"Health: {health}")