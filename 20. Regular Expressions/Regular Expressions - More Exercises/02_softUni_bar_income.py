import re

line = input()
pattern = r"%([A-Z][a-z]*)%[^|$%.]*?<(\w+)>[^|$%.]*?\|(\d+)\|[^|$%.]*?([0-9]+(\.[0-9]+)?)\$"

total = 0

while line != "end of shift":
    match = re.finditer(pattern, line)

    for index in match:
        name = index.group(1)
        item = index.group(2)
        quantity = int(index.group(3))
        price = float(index.group(4))
        temp_total = price * quantity
        total += temp_total
        print(f'{name}: {item} - {temp_total:.2f}')

    line = input()

print(f"Total income: {total:.2f}")