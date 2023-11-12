sequence_of_letters = input()

string_to_print = ""
last_char = ""

for char in sequence_of_letters:
    if char != last_char:
        string_to_print += char
        last_char = char

print(string_to_print)
