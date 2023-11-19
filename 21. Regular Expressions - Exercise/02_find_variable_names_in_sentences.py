import re
line = input()
pattern = r"\b_([A-Za-z0-9]+)\b"
match = re.findall(pattern, line)
print(",".join(match))
