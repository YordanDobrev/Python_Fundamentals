def words(action, start, end, raw_text):
    if action == "Upper":
        raw_text = raw_text[:start] + raw_text[start:end].upper() + raw_text[end:]
        return raw_text
    elif action == "Lower":
        raw_text = raw_text[:start] + raw_text[start:end].lower() + raw_text[end:]
        return raw_text


raw_key = input()
command = input()

while command != "Generate":
    current_command = command.split(">>>")
    action = current_command[0]

    if action == "Contains":
        substring = current_command[1]
        if substring in raw_key:
            print(f"{raw_key} contains {substring}")
        else:
            print("Substring not found!")

    elif action == "Flip":
        upper_or_lower = current_command[1]
        start_index = int(current_command[2])
        end_index = int(current_command[3])
        raw_key = words(upper_or_lower, start_index, end_index, raw_key)
        print(raw_key)

    elif action == "Slice":
        first_index = int(current_command[1])
        second_index = int(current_command[2])
        raw_key = raw_key[:first_index] + raw_key[second_index:]
        print(raw_key)
    command = input()

print(f"Your activation key is: {raw_key}")
