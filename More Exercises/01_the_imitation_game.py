message = input()
command = input()

while command != "Decode":
    current_line = command.split("|")
    if current_line[0] == "ChangeAll":
        while current_line[1] in message:
            message = message.replace(current_line[1], current_line[2])

    elif current_line[0] == "Insert":
        index = int(current_line[1])
        message = message[:index] + current_line[2] + message[index:]

    elif current_line[0] == "Move":
        index = int(current_line[1])
        message = message[index:] + message[:index]
    command = input()

print(f"The decrypted message is: {message}")
