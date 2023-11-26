cities = {}
line = input()

while line != "Sail":
    current_line = line.split("||")
    current_city = current_line[0]
    current_population = int(current_line[1])
    current_gold = int(current_line[2])

    if current_city in cities.keys():
        cities[current_city]["population"] += current_population
        cities[current_city]["gold"] += current_gold
    else:
        cities[current_city] = {"population": current_population, "gold": current_gold}

    line = input()

command = input()

while command != "End":
    current_command = command.split("=>")
    action = current_command[0]
    town = current_command[1]

    if action == "Plunder":
        people_killed = int(current_command[2])
        gold_plundered = int(current_command[3])
        cities[town]["population"] -= people_killed
        cities[town]["gold"] -= gold_plundered
        print(f"{town} plundered! {gold_plundered} gold stolen, {people_killed} citizens killed.")
        if cities[town]["population"] <= 0 or cities[town]["gold"] <= 0:
            cities.pop(town)
            print(f"{town} has been wiped off the map!")

    elif action == "Prosper":
        gold_prosper = int(current_command[2])
        if gold_prosper < 0:
            print("Gold added cannot be a negative number!")
            command = input()
            continue
        cities[town]["gold"] += gold_prosper
        print(f"{gold_prosper} gold added to the city treasury. {town} now has {cities[town]['gold']} gold.")

    command = input()

if len(cities) == 0:
    print(f"Ahoy, Captain! All targets have been plundered and destroyed!")
else:
    print(f"Ahoy, Captain! There are {len(cities)} wealthy settlements to go to:")
    for towns in cities:
        print(f"{towns} -> Population: {cities[towns]['population']} citizens, Gold: {cities[towns]['gold']} kg")
