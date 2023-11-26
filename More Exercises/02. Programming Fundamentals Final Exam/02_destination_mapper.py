import re

some_text = input()
valid_locations = []
points = 0
pattern = r"([=\/])([A-Z][A-Za-z]{2,})\1"

match = re.findall(pattern, some_text)

for index in match:
    valid_locations.append(index[1])
    points += len(index[1])

print(f"Destinations: {', '.join(valid_locations)}")
print(f"Travel Points: {points}")
