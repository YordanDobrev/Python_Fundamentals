import re

command = input()
pattern = r">>([A-Za-z]+)<<([0-9]+\.?[0-9?]+)!([0-9]+)"
total = 0
items = []

while command != "Purchase":
    match = re.search(pattern, command)
    if match:
        furniture, price, quantity = match.groups()
        total += float(price) * int(quantity)
        items.append(furniture)
    command = input()

print(f"Bought furniture:")
for index in items:
    print(index)
print(f"Total money spend: {total:.2f}")
