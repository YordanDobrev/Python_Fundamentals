# Read User Input
items_with_their_prices = input().split("|")
budget = float(input())

# Logic
new_list = []
profit = 0

for i in range(len(items_with_their_prices)):
    current_item = items_with_their_prices[i].split("->")
    item = current_item[0]
    price = float(current_item[1])

    if item == "Clothes" and price <= 50.00 and budget - price >= 0:
        new_list.append(round(price * 1.40, 2))
        budget -= price
        profit += (price * 1.40) - price
    elif item == "Shoes" and price <= 35.00 and budget - price >= 0:
        new_list.append(round(price * 1.40, 2))
        budget -= price
        profit += (price * 1.40) - price
    elif item == "Accessories" and price <= 20.50 and budget - price >= 0:
        new_list.append(round(price * 1.40, 2))
        budget -= price
        profit += (price * 1.40) - price

# Print Output

for i in range(len(new_list)):
    print(f"{new_list[i]:.2f}", end=' ')

print()
print(f"Profit: {profit:.2f}")

if sum(new_list) + budget >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")