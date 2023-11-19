import re

line = input()
pattern = r"\d+"

while line:
    match = re.finditer(pattern, line)

    for index in match:
        print(index.group(), end=" ")

    line = input()
