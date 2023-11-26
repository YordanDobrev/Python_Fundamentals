number_of_plants = int(input())
plants = {}

for index in range(number_of_plants):
    command = input().split("<->")
    plant = command[0]
    rarity = int(command[1])

    if plant in plants.keys():
        plants[plant]["rarity"] = rarity
    else:
        plants[plant] = {"rarity": rarity, "rating": 0, "count": 0}

line = input()

while line != "Exhibition":
    current_line = line.split()
    action = current_line[0]
    current_plant = current_line[1]

    if current_plant not in plants.keys():
        print("error")

    elif action == "Rate:":
        current_rating = float(current_line[3])
        plants[current_plant]["rating"] += current_rating
        plants[current_plant]["count"] += 1

    elif action == "Update:":
        new_rarity = int(current_line[3])
        plants[current_plant]["rarity"] = new_rarity

    elif action == "Reset:":
        plants[current_plant]["rating"] = 0

    line = input()

print("Plants for the exhibition:")

for key, value in plants.items():
    if value["count"] <= 1:
        print(f"- {key}; Rarity: {value['rarity']}; Rating: {value['rating']:.2f}")
    else:
        average_rating = value["rating"] / value["count"]
        print(f"- {key}; Rarity: {value['rarity']}; Rating: {average_rating:.2f}")
