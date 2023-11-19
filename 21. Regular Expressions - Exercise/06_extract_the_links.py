import re

links = input()
pattern = r"www\.[A-Za-z0-9\-]+\.[a-z\.]+"

while links:
    match = re.findall(pattern, links)
    if match:
        for index in match:
            print(index)
    links = input()