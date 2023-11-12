string = input()
new_string = ""
strength = 0

for index in range(len(string)):
    current_index = string[index]
    if strength > 0 and string[index] != ">":
        strength -= 1
    elif string[index] == ">":
        new_string += string[index]
        strength += int(string[index + 1])
    else:
        new_string += current_index

print(new_string)