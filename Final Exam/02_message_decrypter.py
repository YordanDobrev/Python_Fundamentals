import re

number_of_messages = int(input())
valid_numbers = []
text_to_extract = ""
pattern = r"^([$%])([A-Z][a-z]{2,})\1:\s\[(\d+)\]\|\[(\d+)\]\|\[(\d+)\]\|$"

for index in range(number_of_messages):
    line = input()
    match = re.findall(pattern, line)
    if match:
        valid_numbers.append(match)
    else:
        valid_numbers.append("Valid message not found!")

for messages in range(len(valid_numbers)):
    if valid_numbers[messages] == "Valid message not found!":
        print(valid_numbers[messages])
    else:
        for x in valid_numbers[messages]:
            tag = x[1]
            letters = chr(int(x[2])) + chr(int(x[3])) + chr(int(x[4]))
            print(f"{tag}: {letters}")
