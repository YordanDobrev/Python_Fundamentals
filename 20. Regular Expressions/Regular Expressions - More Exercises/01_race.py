import re

participants = input().split(", ")
racers = {}
for index in participants:
    racers[index] = 0

name_pattern = r"[A-Za-z]"
number_pattern = r"[0-9]"

command = input()

while command != "end of race":
    total_number = 0

    name_match = re.findall(name_pattern, command)
    number_match = re.findall(number_pattern, command)
    current_racer = "".join(name_match)

    if current_racer not in racers.keys():
        command = input()
        continue

    for current_index in number_match:
        total_number += int(current_index)

    racers[current_racer] += total_number

    command = input()

top = 1
for i in sorted(racers, key=racers.get, reverse=True):
    if top == 1:
        print(f"1st place: {i}")
    elif top == 2:
        print(f"2nd place: {i}")
    elif top == 3:
        print(f"3rd place: {i}")
    top += 1
    if top == 4:
        break
