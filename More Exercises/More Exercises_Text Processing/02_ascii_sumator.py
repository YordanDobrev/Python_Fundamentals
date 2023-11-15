first_char = ord(input())
second_char = ord(input())
line = input()

total = 0

for index in range(len(line)):
    current_symbol_check = line[index]
    current_symbol = ord(line[index])
    if first_char < current_symbol < second_char:
        total += current_symbol

print(total)
