courses = {}

command = input()

while command != "end":
    current_command = command.split(" : ")
    current_course = current_command[0]
    name = current_command[1]

    if current_course not in courses.keys():
        courses[current_course] = []
        courses[current_course].append(name)
    else:
        courses[current_course].append(name)

    command = input()

for course, name in courses.items():
    print(f"{course}: {len(name)}")
    for i in range(len(name)):
        print(f"-- {name[i]}")
