the_string = input()
command = input()

while command != "Done":
    current_command = command.split()
    action = current_command[0]

    if action == "Change":
        char = current_command[1]
        replacement = current_command[2]
        the_string = the_string.replace(char, replacement)
        print(the_string)

    elif action == "Includes":
        substring = current_command[1]
        if substring in the_string:
            print("True")
        else:
            print("False")

    elif action == "End":
        substring_ends = current_command[1]
        if the_string.endswith(substring_ends):
            print("True")
        else:
            print("False")

    elif action == "Uppercase":
        the_string = the_string.upper()
        print(the_string)

    elif action == "FindIndex":
        find_char = current_command[1]
        print(the_string.find(find_char))

    elif action == "Cut":
        start_index = int(current_command[1])
        cut = int(current_command[2])
        the_string = the_string[start_index:(start_index + cut)]
        print(the_string)

    command = input()
