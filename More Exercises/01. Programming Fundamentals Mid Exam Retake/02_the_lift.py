people = int(input())
wagon = input().split()
no_more_people = False

for i in range(len(wagon)):
    current_wagon = int(wagon[i])

    while current_wagon < 4:
        if people > 0:
            current_wagon += 1
            people -= 1
        else:
            no_more_people = True
            break

    wagon[i] = str(current_wagon)

    if people == 0:
        no_more_people = True
        break

if no_more_people:
    print(f"The lift has empty spots!\n"
          f"{' '.join(str(e) for e in wagon)}")
else:
    print(f"There isn't enough space! {people} people in a queue!\n"
          f"{' '.join(str(e) for e in wagon)}")