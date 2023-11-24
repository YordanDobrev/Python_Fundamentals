number_of_cars = int(input())
cars = []

for index in range(number_of_cars):
    current_line = input().split("|")
    model = current_line[0]
    mileage = int(current_line[1])
    fuel = int(current_line[2])

    line = {"model": model, "mileage": mileage, "fuel": fuel}
    cars.append(line)

command = input()

while command != "Stop":
    current_command = command.split(" : ")
    action = current_command[0]
    car_model = current_command[1]

    if action == "Drive":
        distance = int(current_command[2])
        given_fuel = int(current_command[3])

        for car in cars:
            if car["model"] == car_model:
                if given_fuel > car["fuel"]:
                    print("Not enough fuel to make that ride")
                    break
                else:
                    car["fuel"] = car["fuel"] - given_fuel
                    car["mileage"] += distance
                    print(f"{car_model} driven for {distance} kilometers. {given_fuel} liters of fuel consumed.")
                    if car["mileage"] >= 100000:
                        print(f"Time to sell the {car_model}!")
                        del car["fuel"], car["mileage"], car["model"]
                        cars.remove(car)
                    break

    elif action == "Refuel":
        fuel_to_refill = int(current_command[2])
        for all_cars in cars:
            temp_fuel = all_cars["fuel"]
            max_tank = 75
            if all_cars["model"] == car_model:
                all_cars["fuel"] += fuel_to_refill
                if temp_fuel + fuel_to_refill > 75:
                    all_cars["fuel"] = max_tank
                refueled_amount = all_cars["fuel"] - temp_fuel
                print(f"{car_model} refueled with {refueled_amount} liters")
                break

    elif action == "Revert":
        kilometers = int(current_command[2])

        for revert_car in cars:
            if revert_car["model"] == car_model:
                revert_car["mileage"] -= kilometers
                print(f"{car_model} mileage decreased by {kilometers} kilometers")
                if revert_car["mileage"] < 10000:
                    revert_car["mileage"] = 10000
                break
    command = input()

for all_cars in cars:
    print(f"{all_cars['model']} -> Mileage: {all_cars['mileage']} kms, Fuel in the tank: {all_cars['fuel']} lt.")