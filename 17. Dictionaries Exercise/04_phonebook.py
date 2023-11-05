address_book = {}

command = input()

while len(command) > 5:
    current_address = command.split("-")
    address_book[current_address[0]] = current_address[1]

    command = input()

for names in range(int(command)):
    current_name = input()

    if current_name in address_book.keys():
        print(f"{current_name} -> {address_book[current_name]}")
    else:
        print(f"Contact {current_name} does not exist.")
