energy = int(input())
battles_won = 0

command = input()
enough_energy = True

while command != "End of battle":
    distance = int(command)

    if energy < distance:
        print(f"Not enough energy! Game ends with {battles_won} won battles and {energy} energy")
        enough_energy = False
        break
    else:
        energy -= distance
        battles_won += 1

    if battles_won % 3 == 0:
        energy += battles_won

    command = input()

if enough_energy:
    print(f"Won battles: {battles_won}. Energy left: {energy}")
