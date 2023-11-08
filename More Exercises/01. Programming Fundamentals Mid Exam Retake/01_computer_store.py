command = input()
total = 0
taxes = 0

while True:
    if command == "special" or command == "regular":
        break

    current_number = float(command)

    if current_number < 0:
        print(f"Invalid price!")
        command = input()
        continue

    total += current_number
    command = input()

if total == 0:
    print("Invalid order!")
    exit()

taxes = total * 0.20

print(f"Congratulations you've just bought a new computer!")
print(f"Price without taxes: {total:.2f}$")
print(f"Taxes: {taxes:.2f}$")
print(f"-----------")

final_price = total + taxes
if command == "special":
    final_price *= 0.90

print(f"Total price: {final_price:.2f}$")
