import re

line = input()
pattern = r"\s(([a-z0-9]+[a-z0-9\.\-\_]*)@([a-z\-]+)(\.[a-z]+)+)\b"
match = re.finditer(pattern, line)

for index in match:
    print(index.group(1))