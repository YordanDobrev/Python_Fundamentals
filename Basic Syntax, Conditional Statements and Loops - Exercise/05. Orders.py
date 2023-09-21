#Read User Input
order = int(input())

#Logic

total = 0

for i in range(order):
    price_per_capsule = float(input())
    days = int(input())
    capsules_per_day = int(input())
    if days < 1 or days > 31 or \
            capsules_per_day < 1 or capsules_per_day > 2000 or \
            price_per_capsule < 0.01 or price_per_capsule > 100.00:
        continue
    order_total = (days * capsules_per_day) * price_per_capsule
    print(f"The price for the coffee is: ${order_total:.2f}")
    total += order_total

#Print Output

print(f"Total: ${total:.2f}")