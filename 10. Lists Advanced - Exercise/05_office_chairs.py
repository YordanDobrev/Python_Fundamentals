# Read User Input
number_of_rooms = int(input())

# Logic

free_chairs = 0
ready = True

for i in range(1, number_of_rooms + 1):
    command = input().split()
    chairs = len(command[0])
    peoples = int(command[1])
    difference = abs(chairs - peoples)

    if chairs >= peoples:
        free_chairs += difference
    elif chairs < peoples:
        ready = False
        print(f"{difference} more chairs needed in room {i}")

# Print Output

if ready:
    print(f"Game On, {free_chairs} free chairs left")