import re

text = input()

regex = r"(^|(?<=\s))-?([0]|[1-9][0-9]*)(\.\d+)?($|(?=\s))"

match = re.finditer(regex, text)

for index in match:
    print(index.group(), end=" ")