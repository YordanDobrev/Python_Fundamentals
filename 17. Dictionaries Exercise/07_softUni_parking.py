parking = {}

cars = int(input())

for i in range(cars):
    current_car = input().split()

    if current_car[1] in parking.keys() and current_car[0] == "register":
        print(f"ERROR: already registered with plate number {current_car[2]}")
    elif current_car[1] not in parking.keys() and current_car[0] == "register":
        parking[current_car[1]] = current_car[2]
        print(f"{current_car[1]} registered {current_car[2]} successfully")

    if current_car[1] not in parking.keys() and current_car[0] == "unregister":
        print(f"ERROR: user {current_car[1]} not found")
    elif current_car[1] in parking.keys() and current_car[0] == "unregister":
        del parking[current_car[1]]
        print(f"{current_car[1]} unregistered successfully")

for name, registration in parking.items():
    print(f"{name} => {registration}")
