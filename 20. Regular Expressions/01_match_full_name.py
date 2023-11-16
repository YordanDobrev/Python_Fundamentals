import re

text = input()

pattern = r"\b[A-Z]{1}[a-z]+\b \b[A-Z]{1}[a-z]+\b"

match = re.findall(pattern, text)

print(" ".join(match))