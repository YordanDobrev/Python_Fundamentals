# Read User Input
order = input()
quantity = int(input())


# Logic


def orders_calculation(order_type, amount):
    if order_type == "coffee":
        return amount * 1.50
    elif order_type == "water":
        return amount * 1.00
    elif order_type == "coke":
        return amount * 1.40
    elif order_type == "snacks":
        return amount * 2.00


# Print Output

print(f"{orders_calculation(order, quantity):.2f}")
