resources = {"shards": 0, "fragments": 0, "motes": 0}

legendary_item_created = False

while True:
    if legendary_item_created is True:
        break

    line = input().lower().split()

    for i in range(0, len(line), 2):
        quantity = int(line[i])
        material = line[i + 1]
        if material not in resources.keys():
            resources[material] = quantity
        else:
            resources[material] += quantity

        if resources["shards"] >= 250:
            resources["shards"] -= 250
            legendary_item_created = True
            print(f"Shadowmourne obtained!")
            break

        if resources["fragments"] >= 250:
            resources["fragments"] -= 250
            legendary_item_created = True
            print(f"Valanyr obtained!")
            break

        if resources["motes"] >= 250:
            resources["motes"] -= 250
            legendary_item_created = True
            print(f"Dragonwrath obtained!")
            break

for material, quantity in resources.items():
    print(f"{material}: {quantity}")