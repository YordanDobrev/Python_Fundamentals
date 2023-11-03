def to_print():
    print(f"Products in stock:")
    for products, quantity in bakery.items():
        print(f"- {products}: {quantity}")
    print(f"Total Products: {len(bakery)}")
    print(f"Total Quantity: {sum(bakery.values())}")


bakery = {}

while True:
    command = input()

    if command == "statistics":
        break

    command = command.split(": ")

    if command[0] not in bakery:
        bakery[command[0]] = int(command[1])
    else:
        bakery[command[0]] += int(command[1])

to_print()
