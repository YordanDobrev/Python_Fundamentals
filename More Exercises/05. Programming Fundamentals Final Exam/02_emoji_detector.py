import re

pattern = r"((\:{2})([A-Z][a-z]{2,})\2)|((\*{2})([A-Z][a-z]{2,})\5)"
emojis = []
text = input()
coolness = 1
match = re.finditer(pattern, text)

for i in match:
    if "::" in i.groups():
        emojis.append(i.group(1))
    elif "**" in i.groups():
        emojis.append(i.group(4))

for cool in range(len(text)):
    current_char = text[cool]
    if text[cool].isnumeric():
        coolness *= int(text[cool])

print(f"Cool threshold: {coolness}")
print(f"{len(emojis)} emojis found in the text. The cool ones are:")

for current_emoji in emojis:
    total_ascii = 0
    for i in range(len(current_emoji)):
        if current_emoji[i] == ":" or current_emoji[i] == "*":
            continue
        total_ascii += ord(current_emoji[i])
    if total_ascii >= coolness:
        print(current_emoji)