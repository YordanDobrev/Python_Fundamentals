import re
text = input()
regex = r"\+\b[359]+ 2 [0-9]{3} [0-9]{4}\b|\+\b[359]+-2-[0-9]{3}-[0-9]{4}\b"
match = re.findall(regex, text)
print(", ".join(match))
