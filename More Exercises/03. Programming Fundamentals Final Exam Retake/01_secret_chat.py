concealed_message = input()
command = input()

while command != "Reveal":
    current_command = command.split(":|:")
    action = current_command[0]

    if action == "InsertSpace":
        index = int(current_command[1])
        concealed_message = concealed_message[:index] + " " + concealed_message[index:]

    elif action == "Reverse":
        substring = current_command[1]
        if substring not in concealed_message:
            print("error")
            command = input()
            continue
        cut = concealed_message.find(substring)
        reversed_word = substring[::-1]
        concealed_message = concealed_message[:cut] + reversed_word

    elif action == "ChangeAll":
        substring_to_change = current_command[1]
        replacement = current_command[2]
        concealed_message = concealed_message.replace(substring_to_change, replacement)

    print(concealed_message)
    command = input()

print(f"You have a new text message: {concealed_message}")
