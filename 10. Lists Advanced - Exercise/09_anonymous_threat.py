string = input().split()
command = input()

while command != "3:1":
    current_command = command.split()
    action = current_command[0]

    if action == "merge":
        start_index = int(current_command[1])
        end_index = int(current_command[2])
        if start_index < 0:
            start_index = 0
        if end_index > len(string) - 1:
            end_index = len(string) - 1
        merged_elements = "".join(string[start_index:end_index + 1])
        string[start_index:end_index + 1] = [merged_elements]

    elif action == "divide":
        index = int(current_command[1])
        partitions = int(current_command[2])



    command = input()

print(string)