# Read User Input
initial_energy = 100
initial_coins = 100
working_day_events = input().split("|")

# Logic
bakery_closed = False

for i in range(len(working_day_events)):
    event = working_day_events[i].split("-")
    current_event = event[0]
    event_number = int(event[1])

    if current_event == "rest":
        temp_energy = initial_energy
        initial_energy += event_number

        if initial_energy >= 100:
            initial_energy = 100
        gained_energy = initial_energy - temp_energy
        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {initial_energy}.")

    elif current_event == "order":
        if initial_energy >= 30:
            initial_energy -= 30
            initial_coins += event_number
            print(f"You earned {event_number} coins.")
        else:
            initial_energy += 50
            print("You had to rest!")
            continue

    else:
        if initial_coins >= event_number:
            initial_coins -= event_number
            print(f"You bought {current_event}.")
        else:
            print(f"Closed! Cannot afford {current_event}.")
            bakery_closed = True
            break

# Print Output
if not bakery_closed:
    print("Day completed!")
    print(f"Coins: {initial_coins}")
    print(f"Energy: {initial_energy}")