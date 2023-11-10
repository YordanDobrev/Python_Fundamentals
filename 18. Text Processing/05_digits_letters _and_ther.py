line = input()

digit = ""
letter = ""
other = ""

for symbol in line:
    if symbol.isdigit():
        digit += symbol
    elif symbol.isalpha():
        letter += symbol
    else:
        other += symbol

print(digit)
print(letter)
print(other)

