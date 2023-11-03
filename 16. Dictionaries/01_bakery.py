bakery = {}

line = input().split()

for i in range(0, len(line), 2):
    product = line[i]
    quantity = line[i + 1]
    bakery[product] = int(quantity)

print(bakery)