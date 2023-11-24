def plunder(some_town, some_people, some_gold):
    for keys, values in targets.items():
        town_population = values[0] - some_people
        town_gold = values[1] - some_gold

        if town_population < 0 or town_gold < 0:
            del targets[some_town]
            print(f"{some_town} has been wiped off the map!")
        else:
            targets[some_town] = [town_population, town_gold]
            print(f"{some_town} plundered! {some_gold} gold stolen, {some_people} citizens killed.")


def prosper(given_town, given_gold):
    if given_gold < 0:
        print("Gold added cannot be a negative number!")
        return targets[given_town]
    temp_people = targets[given_town][0]
    the_gold = targets[given_town][1] + given_gold
    targets[given_town] = [temp_people, the_gold]
    print(f"{given_gold} gold added to the city treasury. {given_town} now has {the_gold} gold.")
    return targets[given_town]


targets = {}
command = input()
while command != "Sail":
    current_command = command.split("||")
    current_city = current_command[0]
    current_population = int(current_command[1])
    current_gold = int(current_command[2])

    if current_city in targets.keys():
        temp_population = targets[current_city][0] + current_population
        temp_gold = targets[current_city][1] + current_gold
        targets[current_city] = [temp_population, temp_gold]
    else:
        targets[current_city] = [current_population, current_gold]
    command = input()

# -------------------READY -----------------------------------

event = input()

while event != "End":
    current_command = event.split("=>")
    action = current_command[0]
    town = current_command[1]

    if action == "Plunder":
        people = int(current_command[2])
        gold = int(current_command[3])
        plunder(town, people, gold)

    elif action == "Prosper":
        gold = int(current_command[2])
        prosper(town, gold)

    event = input()
# -------------------READY ----------------------------------

print("Ahoy, Captain! All targets have been plundered and destroyed!")

for key, value in targets.items():
    print(f"{key} -> Population: {value[0]} citizens, Gold: {value[1]} kg")
