characters = {}

the_line = [char for char in input() if char != " "]

for this_char in the_line:
    if this_char not in characters.keys():
        characters[this_char] = 0
    characters[this_char] += 1

for letter, count in characters.items():
    print(f"{letter} -> {count}")
