lines = int(input())

for current_line in range(lines):
    command = input()
    name_start = command.find("@")
    name_end = command.find("|")
    age_start = command.find("#")
    age_end = command.find("*")

    name = command[name_start + 1: name_end]
    age = command[age_start + 1: age_end]

    print(f"{name} is {age} years old.")
