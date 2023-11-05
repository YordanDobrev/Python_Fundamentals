stock = {}
stock_quantity = {}

command = input()

while command != "buy":
    line = command.split()
    product = line[0]
    price = float(line[1])
    quantity = int(line[2])

    stock[product] = price

    if product not in stock_quantity.keys():
        stock_quantity[product] = quantity
    else:
        stock_quantity[product] += quantity

    command = input()

for product, price in stock.items():
    print(f"{product} -> {price * stock_quantity[product]:.2f}")
