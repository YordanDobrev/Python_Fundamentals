import re
text = input()
regex = r"\b([0-9]{2})([-.\/])([A-Z][a-z]{2})\2([0-9]{4})"
match = re.findall(regex, text)

for index in match:
    day = index[0]
    month = index[2]
    year = index[3]
    print(f"Day: {day}, Month: {month}, Year: {year}")
