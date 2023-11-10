command = input()

while command != "end":
    new_text = command[::-1]
    print(f"{command} = {new_text}")

    command = input()