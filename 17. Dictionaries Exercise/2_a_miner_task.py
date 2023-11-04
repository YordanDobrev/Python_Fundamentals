mine = {}

while True:
    command = input()

    if command == "stop":
        break

    quantity = int(input())
    if command not in mine.keys():
        mine[command] = 0
    mine[command] += quantity

for resource, quantity in mine.items():
    print(f"{resource} -> {quantity}")
