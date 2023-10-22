# Read User Input
vehicles = input().split(">>")

# Logic
total = 0
for i in range(len(vehicles)):
    current_car = vehicles[i].split()
    car_type = current_car[0]
    car_year = int(current_car[1])
    car_kilometers = int(current_car[2])

    if car_type == "family":
        initial_tax = 50 - (car_year * 5) + ((car_kilometers // 3000) * 12)
        total += initial_tax
        print(f"A {car_type} car will pay {initial_tax:.2f} euros in taxes.")
    elif car_type == "heavyDuty":
        initial_tax = 80 - (car_year * 8) + ((car_kilometers // 9000) * 14)
        total += initial_tax
        print(f"A {car_type} car will pay {initial_tax:.2f} euros in taxes.")
    elif car_type == "sports":
        initial_tax = 100 - (car_year * 9) + ((car_kilometers // 2000) * 18)
        total += initial_tax
        print(f"A {car_type} car will pay {initial_tax:.2f} euros in taxes.")
    else:
        print(f"Invalid car type.")
        continue

# Print Output

print(f"The National Revenue Agency will collect {total:.2f} euros in taxes.")





#  family 3 7210>>van 4 2345>>heavyDuty 9 31000>>sports 4 7410