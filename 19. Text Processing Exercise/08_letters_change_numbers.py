alphabet = {}
index = 0
for letter in range(97, 123):
    index += 1
    alphabet[chr(letter)] = index

line = input().split()
total = 0

for word in line:
    current_word = word
    letters = ""
    current_number = ""
    temp_total = 0
    for index in current_word:
        if index.isalpha():
            letters += index
        else:
            current_number += index

    if letters[0].isupper():
        temp_total = int(current_number) / alphabet[letters[0].lower()]
    else:
        temp_total = int(current_number) * alphabet[letters[0].lower()]

    if letters[1].islower():
        temp_total += alphabet[letters[1].lower()]
    else:
        temp_total -= alphabet[letters[1].lower()]

    total += temp_total

print(f"{total:.2f}")
